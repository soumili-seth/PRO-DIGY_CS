def encrypt_image(image, operation, key):
    
    encrypted_image = Image.new(image.mode, image.size)
    pixels = image.load()
    encrypted_pixels = encrypted_image.load()
    
    for x in range(image.width):
        for y in range(image.height):
            pixel = pixels[x, y]
            
            if operation == "ADD":
                encrypted_pixel = tuple((i + key) % 256 for i in pixel)
            elif operation == "SUB":
                encrypted_pixel = tuple((i - key) % 256 for i in pixel)
            elif operation == "MUL":
                encrypted_pixel = tuple((i * key) % 256 for i in pixel)
            elif operation == "DIV":
                encrypted_pixel = tuple((i // key) % 256 for i in pixel)
            elif operation == "SWAP":
                encrypted_pixel = (pixel[2], pixel[1], pixel[0])
            
            encrypted_pixels[x, y] = encrypted_pixel
    
    return encrypted_image

def decrypt_image(image, operation, key):
   
    decrypted_image = Image.new(image.mode, image.size)
    pixels = image.load()
    decrypted_pixels = decrypted_image.load()
    
    for x in range(image.width):
        for y in range(image.height):
            pixel = pixels[x, y]
            
            if operation == "ADD":
                decrypted_pixel = tuple((i - key) % 256 for i in pixel)
            elif operation == "SUB":
                decrypted_pixel = tuple((i + key) % 256 for i in pixel)
            elif operation == "MUL":
                decrypted_pixel = tuple((i * pow(key, -1, 256)) % 256 for i in pixel)
            elif operation == "DIV":
                decrypted_pixel = tuple((i * key) % 256 for i in pixel)
            elif operation == "SWAP":
                decrypted_pixel = (pixel[2], pixel[1], pixel[0])
            
            decrypted_pixels[x, y] = decrypted_pixel
    
    return decrypted_image

def main():
    image_path = input("Enter image path: ")
    image = Image.open(image_path)
    
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ")
    
    if choice.upper() == 'E':
        operation = input("Enter encryption operation (ADD, SUB, MUL, DIV, SWAP): ")
        key = int(input("Enter encryption key: "))
        encrypted_image = encrypt_image(image, operation, key)
        encrypted_image.save("encrypted_image.png")
        print("Image encrypted successfully.")
    
    elif choice.upper() == 'D':
        operation = input("Enter decryption operation (ADD, SUB, MUL, DIV, SWAP): ")
        key = int(input("Enter decryption key: "))
        decrypted_image = decrypt_image(image, operation, key)
        decrypted_image.save("decrypted_image.png")
        print("Image decrypted successfully.")
    
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
