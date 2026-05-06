# try:
#     import qrcode
# except ImportError:
#     raise ImportError("Missing required module 'qrcode'. Install it with: pip install qrcode[pil]")
# img=qrcode.make("https://www.youtube.com/channel/UCwfaAHy4zQUb2APNOGXUCDQ")
# img.save("youtube.png")

import qrcode

img = qrcode.make("https://www.youtube.com/channel/UCwfaAHy4zQUb2APNOGXUCDQ")
img.save("youtube.png")
