from StreamDeck.ImageHelpers import PILHelper
from PIL import Image, ImageDraw, ImageFont

def image_from_filename(deck, filename):
    image = PILHelper.create_image(deck)
    draw = ImageDraw.Draw(image)
    
    # Create new key image of the correct dimensions, black background
    image = PILHelper.create_image(deck)
    draw = ImageDraw.Draw(image)

    # Add image overlay, rescaling the image asset if it is too large to fit
    # the requested dimensions via a high quality Lanczos scaling algorithm
    icon = Image.open(filename).convert("RGBA")
    icon.thumbnail((image.width, image.height - 20), Image.LANCZOS)
    icon_pos = ((image.width - icon.width) // 2, 0)
    image.paste(icon, icon_pos, icon)
    return image

def add_text_to_image(font_filename, label_text, image):
    draw = ImageDraw.Draw(image)
    # Load a custom TrueType font and use it to overlay the key index, draw key
    # label onto the image
    font = ImageFont.truetype(font_filename, 14)
    label_w, label_h = draw.textsize(label_text, font=font)
    label_pos = ((image.width - label_w) // 2, image.height - 20)
    draw.text(label_pos, text=label_text, font=font, fill="white")
    return image

