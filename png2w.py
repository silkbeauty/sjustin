import sys
import os
import glob
from PIL import Image

def convert_to_webp(folder, recursive=False):
    # Normalize folder path
    folder = os.path.abspath(folder)

    # Build glob patterns for PNG and JPG/JPEG
    patterns = ["**/*.png", "**/*.jpg", "**/*.jpeg"] if recursive else ["*.png", "*.jpg", "*.jpeg"]
    files = []
    for pattern in patterns:
        files.extend(glob.glob(os.path.join(folder, pattern), recursive=recursive))

    if not files:
        print(f"⚠️ No PNG or JPG files found in '{folder}'")
        return

    print(f"🌀 Converting {len(files)} image files in '{folder}' → WebP ...")

    for file in files:
        try:
            webp_path = file.rsplit(".", 1)[0] + ".webp"
            if os.path.exists(webp_path):
                print(f"⏭️  Skipping (already exists): {webp_path}")
                continue

            image = Image.open(file)
            if image.mode in ("RGBA", "LA"):
                image = image.convert("RGBA")  # preserve alpha if exists
            else:
                image = image.convert("RGB")  # JPGs have no alpha

            image.save(webp_path, "webp", quality=90, method=6)
            print(f"✅ {os.path.basename(file)} → {os.path.basename(webp_path)}")

        except Exception as e:
            print(f"❌ Error converting {file}: {e}")

    print("🎉 Done!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python imgchange.py <folder> [--recursive]")
        sys.exit(1)

    folder = sys.argv[1]
    recursive = "--recursive" in sys.argv

    convert_to_webp(folder, recursive)
