# ================================
# ASCII Art Generator - No Color
# ================================
# HOW TO USE:
# 1. Install Pillow:  pip install Pillow
# 2. Replace "YOUR_IMAGE_PATH" with your image path
#    Example: r"C:\Users\You\Desktop\image.jpg"
# 3. Run the script
# 4. Open output.txt to see your ASCII art
# ================================

from PIL import Image

# --- SETTINGS ---
IMAGE_PATH = "YOUR_IMAGE_PATH"   # ← change this
OUTPUT_FILE = "output.txt"
NEW_WIDTH = 100                  # ← increase for more detail
ASCII_CHARS = " .:-=+*#%@"
# ----------------

image = Image.open(IMAGE_PATH)

width, height = image.size
aspect_ratio = height / width
new_height = int(NEW_WIDTH * aspect_ratio * 0.55)

img = image.resize((NEW_WIDTH, new_height))
img = img.convert("L")
pixels = img.getdata()

chars = [ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels]
chars_joined = "".join(chars)
ascii_rows = [chars_joined[i:i+NEW_WIDTH] for i in range(0, len(chars_joined), NEW_WIDTH)]
ascii_art = "\n".join(ascii_rows)

print(ascii_art)

with open(OUTPUT_FILE, "w") as f:
    f.write(ascii_art)

print(f"\nSaved to {OUTPUT_FILE}")
