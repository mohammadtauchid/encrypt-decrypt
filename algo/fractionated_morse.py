from . import morse

def run(param):
    message, encrypt = param['message'], param['encrypt']
    message = message.lower()

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    trigram = {}
    symbols = ['.', '-', '|']
    x = y = z = 0

    for c in alphabet:
        trigram[c] = symbols[x] + symbols[y] + symbols[z]
        z += 1
        if z == 3:
            z = 0
            y += 1
        if y == 3:
            y = 0
            x += 1

    result = ''
    if encrypt:
        morse_code = list(morse.run({'message': message, 'encrypt': True}).replace(' / ', '||').replace(' ', '|') + '||')
        
        segment = []
        while len(morse_code) > 0:
            seg = ''
            for i in range(3):
                if len(morse_code) == 0:
                    break
                seg += morse_code.pop(0)
            if len(seg) < 3:
                seg += '.' * (3 - len(seg))
            segment.append(seg)

        for seg in segment:
            result += list(trigram.keys())[list(trigram.values()).index(seg)]
    else:
        morse_code = ''
        for i in range(0, len(message), 3):
            morse_code += trigram[message[i]] + trigram[message[i + 1]] + trigram[message[i + 2]]

        morse_code_list = morse_code.split('||')
        if len(morse_code_list[-1]) < 3:
            morse_code_list.pop()

        result = morse.run({'message': ' / '.join(morse_code_list).replace('|', ' '), 'encrypt': False})

    return result.rstrip()
