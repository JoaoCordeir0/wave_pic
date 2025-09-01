from PIL import Image, ImageDraw, ImageFont
import numpy as np
import pytesseract
import textwrap

class ImageService:

    def __init__(self):
        pass

    def generate_image_with_text(self, text: str, size: tuple) -> Image:
        img = Image.new('L', size, color=255)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('DejaVuSans.ttf', 20)

        lines = textwrap.wrap(text, width=40)

        y_text = 25
        for line in lines:
            draw.text((10, y_text), line, fill=0, font=font)
            bbox = draw.textbbox((0, 0), line, font=font)
            line_height = bbox[3] - bbox[1]
            y_text += line_height + 5

        return img
    
    def image_to_text(self, img_array: np.ndarray) -> str:
        reconstructed_img = Image.fromarray(img_array)

        text = pytesseract.image_to_string(reconstructed_img, lang='por')  # ou 'eng'

        return text.strip()