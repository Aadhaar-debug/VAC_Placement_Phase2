from PIL import Image

# Function to encode a message into an image
def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    encoded_img = img.copy()

    binary_message = ''.join(format(ord(char), '08b') for char in message)
    message_index = 0

    for i in range(height):
        for j in range(width):
            pixel = list(img.getpixel((j, i)))
            for color_channel in range(3):
                if message_index < len(binary_message):
                    pixel[color_channel] = pixel[color_channel] & 0xFE | int(binary_message[message_index])
                    message_index += 1
            encoded_img.putpixel((j, i), tuple(pixel))

    encoded_img.save("encoded_image.png")
    print("Message encoded successfully.")

# Function to decode a message from an image
def decode_image(encoded_image_path):
    encoded_img = Image.open(encoded_image_path)
    width, height = encoded_img.size
    binary_message = ""

    for i in range(height):
        for j in range(width):
            pixel = encoded_img.getpixel((j, i))
            for color_channel in range(3):
                binary_message += str(pixel[color_channel] & 1)

    decoded_message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        decoded_message += chr(int(byte, 2))

    return decoded_message

if __name__ == "__main__":
    action = input("Encode (e) or Decode (d)? ")

    if action.lower() == "e":
        image_path = input("Enter image path: ")
        message = input("Enter message to encode: ")
        encode_image(image_path, message)
    elif action.lower() == "d":
        encoded_image_path = input("Enter encoded image path: ")
        decoded_message = decode_image(encoded_image_path)
        print("Decoded message:", decoded_message)
