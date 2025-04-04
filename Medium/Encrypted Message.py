# Encrypt fn to decode message
def encrypt (mssg):
    encrypted_message = ""
    i=1
    for char in mssg.upper():
        if (ord(char) - i )<65 :
            encrypted_message += chr(ord(char) - i + 26)  # Encryption logic by shifting 2 letters for ASCII value less than 65
        else :
            encrypted_message += chr(ord(char) - i)  # Encryption logic by shifting 2 letters

        i+=1
    return encrypted_message

s = input("Enter the message to be encrypted: ")
print("Encrypted message: ", encrypt(s))
