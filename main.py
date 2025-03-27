import sys
import logging
import argparse
import qrcode
import validators

def initialize_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )

def is_valid_url(url):
    if validators.url(url):
        return True
    else:
        logging.error(f"Invalid URL: {url}")
        return False

def generate_qr_code(url, file_path):
    if not is_valid_url(url):
        logging.warning("Invalid URL entered in command line")
        return
    
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
    
        qr.add_data(url)
        qr.make(fit=True)

        code_img = qr.make_image(fill_color="black", back_color="white")

        code_img.save(file_path)
        logging.info(f"QR code saved to {file_path}")

    except Exception as e:
        logging.error(f"Error while generating QR code: {e}")


def main():
    initialize_logging()
    
    parser = argparse.ArgumentParser(description="Generates QR code with encoded URL")
    parser.add_argument('--url', help="The URL to encode in the QR code", default="https://github.com/atwoodmachine")
    args = parser.parse_args()
    generate_qr_code(args.url, 'qr_code.png')

if __name__ == "__main__":
    main()