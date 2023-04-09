from email.mime import image
import qrcode
import os
import image
import xlsxwriter
import urllib.request
qr = qrcode.QRCode(
    version=15,
    box_size=10,
)

webUrl = urllib.request.urlopen(
    '''https://techstorm-23.vercel.app/rules_codebee.html''')
qr.make(fit=True)
img = qr.make_image(fill="black", back_colour="white")
img.save("test.png")
