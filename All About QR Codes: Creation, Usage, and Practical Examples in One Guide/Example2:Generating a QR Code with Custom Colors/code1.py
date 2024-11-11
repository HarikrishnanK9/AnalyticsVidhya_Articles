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

# Create a QR code with custom colors
img_colored = qr.make_image(fill_color='darkgreen', back_color='lightyellow')
img_colored.show()
img_colored.save('custom_color_qr_code.png')
