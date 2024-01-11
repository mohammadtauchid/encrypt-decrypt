def run(message, key, encrypt):
    """Encrypt or decrypt a message using the Caesar cipher.

    :param message: the message to encrypt or decrypt
    :param key: the key to use to encrypt or decrypt
    :param encrypt: True to encrypt, False to decrypt
    :return: the encrypted or decrypted message
    """
    result = ''
    key = int(key)
    if not encrypt:
        key *= -1

    for c in message:
        if c.isupper():
            result += chr((ord(c) + key - 65) % 26 + 65)
        elif c.islower():
            result += chr((ord(c) + key - 97) % 26 + 97)
        else:
            result += c
    
    return result
