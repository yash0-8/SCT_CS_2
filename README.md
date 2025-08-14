# Simple Image Encrypter Tool

This repository includes a straightforward Python script for encrypting and decrypting images. The tool uses pixel manipulation to scramble an image's data, and it shows two basic encryption methods.

## Features

**Channel Swapping:** Encrypts the image by swapping the Red and Blue color channels. This is its own inverse, so executing it again decrypts the image.

**XOR Operation:** Encrypts an image by applying a bitwise XOR operation on each pixel's color values with a secret key. running the process with the same key decrypts the image.

## How to Use

1.  **Clone the Repository:**
    `git clone https://github.com/yash0-8/SCT_CS_2.git`

2.  **Install Dependencies:**
    This script needs the Pillow library. Install it via pip:
    `pip install Pillow`

3.  **Put Your Image:**
    Place your image file of choice in the same folder as the `image_encryption.py` script.

4.  **Modify the Script:**
    Open `image_encryption.py` and modify the `input_file` variable on line 32 to your image's filename. For instance:
    `input_file = "my_photo.jpg"`

5.  **Run the Script:**
    Run the script in your terminal:
    `python image_encryption.py`

The script will output four new image files: two encrypted ones and two decrypted ones, proving the reversibility of the process. 

## Technologies Used

- Python 3.x
- Pillow (Python Imaging Library)
