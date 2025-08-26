# file_modifier.py
# A program to read a file, handle errors, and write a modified version to a new file.

def main():
    input_file = input("Enter the name of the file to read: ")
    output_file = "modified_" + input_file

    try:
        # Open and read the input file
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content (example: uppercase)
        modified_content = content.upper()

        # Write to new file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ Modified file has been saved as {output_file}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
