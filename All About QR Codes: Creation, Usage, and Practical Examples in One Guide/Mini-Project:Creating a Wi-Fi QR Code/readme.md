- Wi-Fi QR codes are an excellent way to allow users to easily connect to a wireless network by simply scanning a code. Instead of manually typing in the Wi-Fi name (SSID) and password, you can generate a QR code that contains all the necessary information, which can be scanned using a smartphone or QR scanner to automatically connect to the network.
- In this guide, I'll show you how to generate a Wi-Fi QR code using Python, which can be particularly useful in public places, offices, or even for personal use. The generated QR code will store Wi-Fi credentials, such as the network name (SSID), password, and security type (e.g., WPA2), allowing devices to connect with ease.
- Inorder to tryout this mini project,1st you have to findout your Wi-Fi SSID,Wi-Fi Security Type and Password using following linux commands in the terminal.Remember , try one after another

### 1 Find the Wi-Fi SSID (Network Name)
- nmcli -t -f active,ssid dev wifi | grep '^yes'

### 2 Get Wi-Fi Security Type
-  here my SSID Name is RAGAI_4G

- nmcli -f ssid,security dev wifi | grep "RAGAI_4G" 

### 3Get Password
- sudo grep -r "psk=" /etc/NetworkManager/system-connections/
