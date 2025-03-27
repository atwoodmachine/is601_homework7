import logging
import argparse
import qrcode
import validators


def is_valid_url(url):
    if validators.url(url):
        return True
    else:
        return False

def generate_qr_code(url, file_path):
    if not is_valid_url(url):
        print("Invalid URL")
        return
    
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
    
        qr.add_data(url)
        qr.make(fit=True)

        code_img = qr.make_image(fill_color="black", back_color="white")

        code_img.save(file_path)

    except Exception as e:
        logging.error(f"Error while generating QR code: {e}")


def main():
    parser = argparse.ArgumentParser(description="Generates QR code with encoded URL")
    parser.add_argument('--url', help="The URL to encode in the QR code", default="https://github.com/atwoodmachine")
    args = parser.parse_args()
    generate_qr_code(args.url, 'qr_code.png')

if __name__ == "__main__":
    main()