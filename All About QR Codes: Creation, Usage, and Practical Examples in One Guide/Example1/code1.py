# pip install qrcode[pil]
import qrcode
from PIL import Image

# Data to be encoded
data = "Welcome to QR Code Tutorial"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # Size of the QR code
    box_size=10,  # Size of each box in the QR code grid
    border=4  # Border thickness
)
qr.add_data(data)
qr.make(fit=True)

# Generate QR code image
img = qr.make_image(fill='black', back_color='white')
img.show()
img.save('simple_qr_code.png')
