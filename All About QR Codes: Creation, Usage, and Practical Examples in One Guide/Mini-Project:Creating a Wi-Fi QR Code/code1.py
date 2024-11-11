# Import the necessary library
import qrcode

# Define Wi-Fi credentials
wifi_ssid = "RAGAI_4G"#replace with your SSID Name
wifi_password = "PASSWORD" #Ur PASSWORD
wifi_security = "WPA2"  # Can be 'WEP', 'WPA', or 'nopass' (no password)

# Create the QR code data in the format that encodes Wi-Fi information
wifi_data = f"WIFI:T:{wifi_security};S:{wifi_ssid};P:{wifi_password};;"

# Create a QR code object with desired settings
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

# Add the Wi-Fi data to the QR code object
qr.add_data(wifi_data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill='black', back_color='white')

# Save the QR code image to a file
img.save('wifi_qr_code.png')

# Display the QR code image (for testing)
img.show()

print("Wi-Fi QR code saved as 'wifi_qr_code.png'")
