from abc import ABC, abstractmethod
from time import sleep

class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"📂 Loading image {self.filename}",  end=" ")
        for _ in range(10):
            sleep(0.25)
            print(".", end="", flush=True)
        print("\n📂 Image loaded")

    def display(self):
        print(f"🖼 Displaying {self.filename}")

class ImageProxy:
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None 

    def display(self):
        if not self._real_image:
            self._real_image = RealImage(self.filename)
        self._real_image.display()

# Usage
image = ImageProxy("cat.jpg")
image.display()  # Loads and displays image
image.display()  # No reloading, just displays
