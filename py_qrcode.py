import pyqrcode

# Recebe o link
link = input("Link para gerar QRcode: ")

# Gera o código QR
url = pyqrcode.create(link)

# Salva o código QR como um arquivo PNG
url.png('qrcode.png', scale=6)
