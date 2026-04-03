choice = int(input("Do you want to cipher (1) or decipher (2) "))

if choice == 1:
    message = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))
    shift = shift % 26
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
    print("Encoded message:", encoded)

if choice == 2:
    message2 = input("Enter encrypted message: ")
    shift2 = int(input("Enter the shift number: "))
    shift2 = shift2 % 26
    decoded = ""
    for char2 in message2:
        if char2.isalpha():
            charnum2 = ord(char2)
            newcharnum2 = charnum2 - shift2
            if char2.isupper() and newcharnum2 < ord('A'):
                newcharnum2 = newcharnum2 + 26
            if char2.islower() and newcharnum2 < ord('a'):
                newcharnum2 = newcharnum2 + 26
            newchar2 = chr(newcharnum2)
            decoded += newchar2 
        else:
            decoded += char2
    print("Decoded message:", decoded)