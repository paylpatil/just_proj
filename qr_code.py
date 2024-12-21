#import qrcode as qr
#img= qr.make("https://www.youtube.com/")
#img.save("YOUTUBE_qr.png")

import qrcode
from PIL import Image

qr= qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=10,border=4,)

qr.add_data("https://www.youtube.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="lavender",back_color="white")
img.save("YOUTUBE_web.png")