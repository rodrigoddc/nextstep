import base64
import io
from PIL import Image


def decode_image(data):
    try:
        data = base64.b64decode(data.encode('UTF-8'))
        buf = io.BytesIO(data)
        img = Image.open(buf)
        return img

    except Exception as e:
        return e
