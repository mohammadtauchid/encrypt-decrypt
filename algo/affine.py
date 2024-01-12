def run(param):
    message, key, encrypt = param

    list_a = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    key = int(key)
    a = list_a[key % len(list_a)]

    if encrypt:
        result = ''
        for c in message:
            if c.islower():
                result += chr((((ord(c) - 97) * a) + key) % 26 + 97)
            elif c.isupper():
                result += chr((((ord(c) - 65) * a) + key) % 26 + 65)
            else:
                result += c
        return result
    else:
        result = ''
        a_inv = [x for x in range(26) if (x * a) % 26 == 1][0]
        for c in message:
            if c.islower():
                result += chr((((ord(c) - 97) - key) * a_inv) % 26 + 97)
            elif c.isupper():
                result += chr((((ord(c) - 65) - key) * a_inv) % 26 + 65)
            else:
                result += c
        return result
