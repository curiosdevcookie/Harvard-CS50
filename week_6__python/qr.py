import os
import qrcode

data = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
image = qrcode.make(data)
image.save("qr.png", "PNG")

data_text = "Hello you!"
image_text = qrcode.make(data_text)
image_text.save("qr_text.png", "PNG")