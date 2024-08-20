from PIL import Image

def encrypt_image(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    # Encrypt the image by modifying the pixel values
    for i in range(img.size[0]):  # width
        for j in range(img.size[1]):  # height
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)  # XOR each pixel with the key

    # Save the encrypted image
    img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(encrypted_image_path, key, output_path):
    # Open the encrypted image
    img = Image.open(encrypted_image_path)
    pixels = img.load()

    # Decrypt the image by reversing the encryption operation
    for i in range(img.size[0]):  # width
        for j in range(img.size[1]):  # height
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)  # XOR again with the same key

    # Save the decrypted image
    img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Example usage
key = int(input("Enter the key for excryption and decryption:    "))

image_path = input("Enter the impage path that you want to encrypt and decrypt:    ")

encrypt_image(image_path, key, 'encrypted_image.png')

decrypt_image('encrypted_image.png', key, 'decrypted_image.png')

