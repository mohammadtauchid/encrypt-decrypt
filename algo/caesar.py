def run(param):
    message, key, encrypt = param
    
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
