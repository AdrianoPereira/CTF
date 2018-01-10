alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def decrypt(cipher, key):
    msg = ''
    cipher = cipher.upper()
    for char in cipher:
        if char in alphabet:
            index = alphabet.find(char) + key
            if index >= 26:
                index -= 26
            msg += alphabet[index]
        else:
            msg += char
    return msg

def encrypt(message, key):
    cipher = ''
    message = message.upper()
    for char in message:
        if char in alphabet:
            index = alphabet.find(char) - key
            if index < 0:
                index += 26
            cipher += alphabet[index]
        else:
            cipher += char
    return cipher

def decryptBruteForce(string):
    for x in range(26):
        print('ROT{}: '.format(x))
        print(decrypt(string, x))

decryptBruteForce(input())
