import sys
import os
import logging
import argparse
from pathlib import Path
from datetime import datetime
import qrcode
import validators
from dotenv import load_dotenv

load_dotenv()

QR_SAVE_DIRECTORY = os.getenv('QR_SAVE_DIRECTORY', 'qr_codes')
FILL_COLOR = os.getenv('FILL_COLOR', 'black')
BACK_COLOR = os.getenv('BACK_COLOR', 'white')

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

def create_directory(path: Path):
    try:
        path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        logging.error(f"Failed to create directory {path}: {e}")
        exit(1)


def generate_qr_code(url, file_path, fill_color, back_color):
    if not is_valid_url(url):
        logging.warning("Invalid URL entered in command line")
        return
    
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
    
        qr.add_data(url)
        qr.make(fit=True)

        code_img = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR)

        code_img.save(file_path)
        logging.info(f"QR code saved to {file_path}")

    except Exception as e:
        logging.error(f"Error while generating QR code: {e}")

def main():
    initialize_logging()

    parser = argparse.ArgumentParser(description="Generates QR code with encoded URL")
    parser.add_argument('--url', help="The URL to encode in the QR code", default="https://github.com/atwoodmachine")
    args = parser.parse_args()

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    qr_code_filename = f"QRCode_{timestamp}.png"

    qr_directory = Path.cwd() / QR_SAVE_DIRECTORY
    qr_file_path = Path.cwd() / QR_SAVE_DIRECTORY / qr_code_filename

    create_directory(qr_directory)

    generate_qr_code(args.url, qr_file_path, FILL_COLOR, BACK_COLOR)

if __name__ == "__main__":
    main()