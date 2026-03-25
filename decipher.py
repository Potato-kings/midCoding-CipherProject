message = input("Enter encrypted message: ")
shift = int(input("Enter the shift number: "))
shift = shift % 26
decoded = ""
for char in message:
    if char.isalpha():
        charnum = ord(char)
        newcharnum = charnum - shift
        newchar = chr(newcharnum)
        decoded += newchar 
    else:
        decoded += char
print("Decoded message:", decoded)
    