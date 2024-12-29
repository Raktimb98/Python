import qrcode
# Data to be encoded in the QR code
# data = "https://www.example.com"
# data = "Raktim Biswas"
data =input("Enter the data to be encoded in the QR code: ")
# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code, range 1 to 40
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Border size (minimum is 4)
)
# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)  # Ensures the entire data fits in the QR code
# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")
# Save the QR code as an image file
img.save("qrcode.png")
# Optionally, display the QR code
img.show()