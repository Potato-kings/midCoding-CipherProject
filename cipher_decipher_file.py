def encode_message(message, shift):
    encoded = ""
    for char in message:
        if char.isalpha():
            charnum = ord(char)
            newcharnum = charnum + shift
            if char.isupper() and newcharnum > ord('Z'):
                newcharnum = newcharnum - 26
            if char.islower() and newcharnum > ord('z'):
                newcharnum = newcharnum - 26
            newchar = chr(newcharnum)
            encoded += newchar 
        else: 
            encoded += char
    return encoded

def decode_message(message, shift):
    decoded = ""
    for char in message:
        if char.isalpha():
            charnum = ord(char)
            newcharnum = charnum - shift
            if char.isupper() and newcharnum < ord('A'):
                newcharnum = newcharnum + 26
            if char.islower() and newcharnum < ord('a'):
                newcharnum = newcharnum + 26
            newchar = chr(newcharnum)
            decoded += newchar 
        else:
            decoded += char
    return decoded


def encode_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as input_handle:
            original_text = input_handle.read()
            encoded = encode_message(original_text, shift)
            print(encoded)

        with open(output_file, 'w') as output_handle:
            output_handle.write(encoded)

        print(f"File '{input_file} was  encoded and saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"File '{input_file}' was not found.")
    except IOError as error:
        print(f"There was a problem working with the file: {error}")

def decode_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as input_handle:
            encoded_text = input_handle.read()
            decoded = decode_message(encoded_text, shift)
            print(decoded)

        with open(output_file, 'w') as output_handle:
            output_handle.write(decoded)

        print(f"File '{input_file} was  decoded and saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"File '{input_file}' was not found.")
    except IOError as error:
        print(f"There was a problem working with the file: {error}")

choice = int(input("Do you want to load text from file to encode (1) or load text from file to decode (2): "))
shift = int(input("Enter the shift number: "))
shift = shift % 26

input_file_path = 'input_file.txt'
output_file_path = 'output_file.txt'

if choice == 1:
    encode_file(input_file_path, output_file_path, shift)

if choice == 2:
    decode_file(input_file_path, output_file_path, shift)
