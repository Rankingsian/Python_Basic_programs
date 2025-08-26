# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"
    
    def move(self):  # polymorphic method
        print("This device can move in its own way.")


# Child Class 1 - Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery
    
    def make_call(self, number):
        print(f"📞 Calling {number} from {self.device_info()}...")
    
    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        print(f"🔋 Battery charged to {self.battery}%")
    
    def move(self):  # overriding move()
        print(f"📱 {self.device_info()} is moving around in your pocket.")


# Child Class 2 - Tablet
class Tablet(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size
    
    def draw(self):
        print(f"✏️ Drawing on the {self.screen_size}-inch {self.device_info()}...")
    
    def move(self):
        print(f"💻 {self.device_info()} is moving in your backpack.")


# Child Class 3 - Smartwatch
class Smartwatch(Device):
    def __init__(self, brand, model, strap_color):
        super().__init__(brand, model)
        self.strap_color = strap_color
    
    def track_steps(self, steps):
        print(f"⌚ {self.device_info()} tracked {steps} steps today!")
    
    def move(self):
        print(f"⌚ {self.device_info()} is moving on your wrist.")


# Create objects
phone = Smartphone("Samsung", "Galaxy S23", 256, 80)
tablet = Tablet("Apple", "iPad Pro", 12.9)
watch = Smartwatch("Fitbit", "Versa 3", "Black")

# Demonstrate features
print("\n--- Device Info ---")
print(phone.device_info())
print(tablet.device_info())
print(watch.device_info())

print("\n--- Unique Features ---")
phone.make_call("0712345678")
tablet.draw()
watch.track_steps(5000)

print("\n--- Polymorphism in Action ---")
devices = [phone, tablet, watch]

for d in devices:
    d.move()   # each device moves differently
