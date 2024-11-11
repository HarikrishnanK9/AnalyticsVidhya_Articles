# !pip install opencv-python
import cv2

# Read the image file
image = cv2.imread('/home/Tutorials/Analytics Vidya/QR_code_with_AnalyticsVidhya_Logo.png')

# Initialize the QR code detector
detector = cv2.QRCodeDetector()

# Detect and decode the QR code
data, vertices_array, _ = detector.detectAndDecode(image)

if vertices_array is not None:
    print(f"Decoded Data: {data}")
else:
    print("QR code not detected.")
