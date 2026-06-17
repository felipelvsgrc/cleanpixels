import os

from PIL import Image


def compress(input_path: str, value: int) -> str:
    file_dir, filename = os.path.split(input_path)
    name, ext = os.path.splitext(filename)

    output_path = os.path.join(file_dir, f"{name}_CleanPixels{ext}")

    with Image.open(input_path) as img:
        if ext.lower() in [".jpeg", ".jpg", ".webp"]:
            if img.mode in ("RGBA", "P") and ext.lower() in [".jpeg", ".jpg"]:
                clean_img = img.convert("RGB")
                clean_img.save(output_path, optimize=True, quality=value)

            else:
                img.save(output_path, optimize=True, quality=value)

        else:
            img.save(output_path, optimize=True, compress_level=value)

    if os.path.getsize(output_path) >= os.path.getsize(input_path):
        os.remove(output_path)

        return ""

    return output_path


def get_extension(file_path: str) -> str:
    _, ext = os.path.splitext(file_path)

    return ext.lower()
