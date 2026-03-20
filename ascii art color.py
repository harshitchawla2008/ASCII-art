# ================================
# ASCII Art Generator - With Color
# ================================
# HOW TO USE:
# 1. Install libraries:  pip install Pillow colorama
# 2. Replace "YOUR_IMAGE_PATH" with your image path
#    Example: r"C:\Users\You\Desktop\image.jpg"
# 3. Run the script
# 4. Colors will show in the terminal
# ================================

from PIL import Image
from colorama import Fore, init
init(autoreset=True)

# --- SETTINGS ---
IMAGE_PATH = "YOUR_IMAGE_PATH"   # ← change this
NEW_WIDTH = 200                  # ← increase for more detail
ASCII_CHARS = " .:-=+*#%@"
# ----------------

image_color = Image.open(IMAGE_PATH)
image = image_color.convert("L")

width, height = image.size
aspect_ratio = height / width
new_height = int(NEW_WIDTH * aspect_ratio * 0.55)

img = image.resize((NEW_WIDTH, new_height))
img = img.convert("L")
pixels = img.getdata()

img_color = image_color.resize((NEW_WIDTH, new_height))
color_pixels = img_color.getdata()

for i, (pixel, color) in enumerate(zip(pixels, color_pixels)):
    r, g, b = color
    char = ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
    if r > 150 and g < 100 and b < 100:
        print(Fore.RED + char, end="")
    elif r > 200 and g > 200 and b > 200:
        print(Fore.WHITE + char, end="")
    elif r < 50 and g < 50 and b < 50:
        print(Fore.BLACK + char, end="")
    else:
        print(Fore.YELLOW + char, end="")
    if (i + 1) % NEW_WIDTH == 0:
        print()
