# My Image Encryption Tool

from PIL import Image
import os
print("Files in this directory:")
print(os.listdir('.'))

# === HELPER FUNCTIONS ===

def manipulate_pixels_xor(image, key):
    """
    Applies a bitwise XOR operation with a key to each pixel's color channels.
    Used for both encryption and decryption.
    """
    processed_image = image.copy()
    pixels = processed_image.load()
    width, height = processed_image.size

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            new_pixel = tuple(channel ^ key for channel in pixel)
            pixels[x, y] = new_pixel
    return processed_image

def manipulate_pixels_swap(image):
    """
    Swaps the red and blue color channels of an image.
    Used for both encryption and decryption.
    """
    if image.mode != 'RGB':
        print("Channel swapping only works on RGB images. Skipping operation.")
        return image
    
    r, g, b = image.split()
    return Image.merge("RGB", (b, g, r))


# === MAIN EXECUTION BLOCK ===

def run_encryption_process(input_path, output_path, operation, key=None):
    """A general-purpose function to run an encryption/decryption task."""
    try:
        img = Image.open(input_path)
        img = img.convert('RGB')
        
        if key is not None:
            processed_img = operation(img, key)
        else:
            processed_img = operation(img)
            
        processed_img.save(output_path)
        print(f"Successfully processed image and saved to '{output_path}'.")
        return True
    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


def main():
    """Manages the full encryption and decryption workflow."""
    
    # --- Configuration ---
    input_file = "Launch_image.jpg"  # Replace with your image filename
    xor_key = 123  # A secret key (0-255) for the XOR operation

    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found. Please place it in the same directory.")
        return
        
    print(f"Using '{input_file}' for the encryption demonstration.")

    # --- Run XOR Encryption and Decryption ---
    print("\n--- Starting XOR Encryption/Decryption ---")
    encrypted_xor_path = "encrypted_xor_" + input_file
    if run_encryption_process(input_file, encrypted_xor_path, manipulate_pixels_xor, xor_key):
        print("Decrypting XOR image...")
        decrypted_xor_path = "decrypted_xor_" + input_file
        run_encryption_process(encrypted_xor_path, decrypted_xor_path, manipulate_pixels_xor, xor_key)

    # --- Run Channel Swap Encryption and Decryption ---
    print("\n--- Starting Channel Swap Encryption/Decryption ---")
    encrypted_swap_path = "encrypted_swap_" + input_file
    if run_encryption_process(input_file, encrypted_swap_path, manipulate_pixels_swap):
        print("Decrypting swapped image...")
        decrypted_swap_path = "decrypted_swap_" + input_file
        run_encryption_process(encrypted_swap_path, decrypted_swap_path, manipulate_pixels_swap)

if __name__ == "__main__":
    main()