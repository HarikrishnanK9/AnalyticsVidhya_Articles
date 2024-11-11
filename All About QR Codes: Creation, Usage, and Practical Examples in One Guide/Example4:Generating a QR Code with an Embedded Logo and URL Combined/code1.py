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

# Open the logo image
logo = Image.open('AV_logo.png')

# Calculate the size for the logo
logo_size = 100  # Set this according to your needs
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality downsampling

# Paste the logo onto the QR code
pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
img.paste(logo, pos, mask=logo)

# Save and show the result
img.save('QR_code_with_AnalyticsVidhya_Logo.png')
img.show()

