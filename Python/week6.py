import requests
import os
import hashlib
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URLs from user
    urls_input = input("Please enter the image URLs (separated by commas): ").strip()
    urls = [url.strip() for url in urls_input.split(',') if url.strip()]
    
    if not urls:
        print("No URLs provided. Exiting.")
        return
    
    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)
    
    # Set to track hashes of downloaded images
    downloaded_hashes = set()
    
    for url in urls:
        try:
            # Validate URL scheme
            if not url.startswith(('http://', 'https://')):
                print(f"✗ Invalid URL scheme (must be HTTP/HTTPS): {url}")
                continue
                
            # Headers to mimic a browser request
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0'
            }
            
            # Send HEAD request first to check headers
            head_response = requests.head(url, headers=headers, timeout=10, allow_redirects=True)
            head_response.raise_for_status()
            
            # Check Content-Type to ensure it's an image
            content_type = head_response.headers.get('Content-Type', '')
            if not content_type.startswith('image/'):
                print(f"✗ URL does not point to an image (Content-Type: {content_type}): {url}")
                continue
                
            # Check Content-Length to avoid large files (e.g., 10MB limit)
            content_length = head_response.headers.get('Content-Length')
            if content_length and int(content_length) > 10 * 1024 * 1024:
                print(f"✗ File too large (over 10MB): {url}")
                continue
                
            # Now, download the image with GET request
            get_response = requests.get(url, headers=headers, timeout=10, stream=True)
            get_response.raise_for_status()
            
            # Read the image content in chunks to compute hash and save
            image_content = b''
            for chunk in get_response.iter_content(chunk_size=8192):
                image_content += chunk
                # Check if we exceed the size limit during download
                if len(image_content) > 10 * 1024 * 1024:
                    print(f"✗ File too large during download (over 10MB): {url}")
                    image_content = b''
                    break
                    
            if not image_content:
                continue  # Skip if empty due to size limit
                
            # Compute SHA-256 hash of the image content
            image_hash = hashlib.sha256(image_content).hexdigest()
            
            # Check for duplicate image
            if image_hash in downloaded_hashes:
                print(f"✓ Duplicate image skipped: {url}")
                continue
                
            # Extract filename from URL or generate from hash
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                # Generate filename from hash and infer extension from Content-Type
                ext = content_type.split('/')[-1]
                if ext.startswith('jpeg') or ext.startswith('jpg'):
                    ext = 'jpg'
                filename = f"{image_hash[:16]}.{ext}"
            else:
                # Sanitize filename to remove any path components
                filename = os.path.basename(filename)
                
            filepath = os.path.join("Fetched_Images", filename)
            
            # Save the image
            with open(filepath, 'wb') as f:
                f.write(image_content)
                
            downloaded_hashes.add(image_hash)
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")
    
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
