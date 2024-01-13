def run(param):
    message, encrypt = param['message'], param['encrypt']

    result = ''
    if encrypt:
        message = message.upper().replace(' ', '')
        for c in message:
            result += str(bin(ord(c) - 65)[2:]).rjust(5, '0').replace('0', 'A').replace('1', 'B') + ' '
    else:
        message = message.upper().split(' ')
        for c in message:
            result += chr(int(c.replace('A', '0').replace('B', '1'), 2) + 65).lower()

    return result.strip()