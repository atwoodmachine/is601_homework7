import qrcode

def main():
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    github_url = "https://github.com/atwoodmachine"
    qr.add_data(github_url)
    qr.make(fit=True)

    code_img = qr.make_image(fill_color="black", back_color="white")

    code_img.save('qr_code.png')

if __name__ == "__main__":
    main()