def run(param):
    message = param['message']
    
    result = ''
    for c in message:
        if c.isupper():
            result += chr((25 - (ord(c) - 65)) + 65)
        elif c.islower():
            result += chr((25 - (ord(c) - 97)) + 97)
        else:
            result += c
    
    return result
