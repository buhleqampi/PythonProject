import qrcode

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename:' ).strip()

qr = qrcode.QRCode()
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')