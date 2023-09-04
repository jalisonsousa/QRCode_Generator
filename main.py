# para importa use:
# pip install qrcode[pil]

import qrcode

# URL que você deseja incluir no QR Code
url = "url aqui"

# Crie o objeto QRCode
qr = qrcode.QRCode(
    version=1,  # Tamanho do QR Code (1 a 40)
    error_correction=qrcode.constants.
    ERROR_CORRECT_L,  # Nível de correção de erro baixo
    box_size=10,  # Tamanho do bloco
    border=4,  # Espaço da borda
)

# Adicione a URL ao QR Code
qr.add_data(url)
qr.make(fit=True)

# Crie uma imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salve a imagem em um arquivo
img.save("qrcode_link.png")

print("QR Code com link criado com sucesso!")
