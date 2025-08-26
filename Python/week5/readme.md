# 📱💻⌚ Smart Device World  

A simple Python project demonstrating **Object-Oriented Programming (OOP)** concepts including **Classes, Inheritance, Encapsulation, and Polymorphism**.  

---

## 🚀 Project Overview  
This project creates a world of smart devices (**Smartphone, Tablet, Smartwatch**) that:  
- Share common attributes and methods via a **parent class** (`Device`)  
- Extend functionality through **child classes**  
- Override methods to implement **polymorphism** (each device moves differently)  
- Encapsulate behaviors (e.g., charging, step tracking, drawing)  

---

## 🏗️ Features  
### ✅ Smartphone  
- Make phone calls  
- Charge battery  
- Moves in your pocket  

### ✅ Tablet  
- Draw on screen  
- Moves in your backpack  

### ✅ Smartwatch  
- Track steps  
- Moves on your wrist  

---

## 🧑‍💻 Code Example  

```python
# Create objects
phone = Smartphone("Samsung", "Galaxy S23", 256, 80)
tablet = Tablet("Apple", "iPad Pro", 12.9)
watch = Smartwatch("Fitbit", "Versa 3", "Black")

# Demonstrate features
print(phone.device_info())       # Inherited method
phone.make_call("0712345678")    # Unique method
tablet.draw()                    # Unique method
watch.track_steps(5000)          # Unique method

# Polymorphism in action
devices = [phone, tablet, watch]
for d in devices:
    d.move()  # Each device overrides move() differently
