import base64
import PIL.Image as Image

_SAVEPATH_BASE64 = "/home/odoo/Documents/Dev/FakePrinter/image_from_base64.jpeg"


def decode_base64_data(encoded_raster_data, width, height):
    # Decode the base64 string back to a byte array
    decoded_bytes = base64.b64decode(encoded_raster_data)
    binary_string = "".join(format(byte, "08b") for byte in decoded_bytes)
    pixels = []

    for y in range(height):
        for x in range(width):
            pixel_value = 0 if binary_string[y * width + x] == "1" else 255
            pixels.append(pixel_value)  # Only grayscale value

    # Create a new image using the reconstructed pixel data
    image = Image.new("L", (width, height))
    image.putdata(pixels)

    image.save(_SAVEPATH_BASE64, "PNG")
