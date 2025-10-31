from PIL import Image
import os
import sys

input_dir = sys.argv[1]  # folder name or path

# Process all images in input_dir
for filename in os.listdir(input_dir):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        continue

    input_path = os.path.join(input_dir, filename)

    # Open image
    with Image.open(input_path) as img:
        w, h = img.size
        new_h = 1080
        new_w = int(w * new_h / h)
        resized = img.resize((new_w, new_h), Image.LANCZOS)
        resized.save(input_path)  # overwrite the original
        print(f"✅ Resized: {filename}")

print("✅ All images processed!")
