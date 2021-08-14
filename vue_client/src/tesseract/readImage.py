try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'


# Simple image to string
print(pytesseract.image_to_string(Image.open('testImage.jpg')))

