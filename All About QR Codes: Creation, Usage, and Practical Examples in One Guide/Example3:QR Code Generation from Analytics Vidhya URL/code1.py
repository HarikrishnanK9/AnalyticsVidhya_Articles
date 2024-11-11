import qrcode
from PIL import Image

# Create the QR code as usual
qr = qrcode.QRCode(
    version=5,  # Version adjusted to accommodate a logo
    box_size=10,
    border=4
)
qr.add_data("https://www.analyticsvidhya.com/")
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill='black', back_color='white')

# Save and show the result
img.save('QR_code_AnalyticsVidhya.png')
img.show()
