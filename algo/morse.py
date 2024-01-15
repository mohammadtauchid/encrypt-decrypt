MORSE_CODE = { 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
               'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
               'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
               'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
               'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
               'z': '--..', '1': '.----', '2': '..---', '3': '...--',
               '4': '....-', '5': '.....', '6': '-....', '7': '--...',
               '8': '---..', '9': '----.', '0': '-----' }

def run(param):
    message, encrypt = param['message'], param['encrypt']

    result = ''
    if encrypt:
        for c in message:
            if c.isspace():
                result += '/ '
            elif c in MORSE_CODE:
                result += MORSE_CODE.get(c.lower()) + ' '
    else:
        for c in message.split(' '):
            if c in MORSE_CODE.values():
                result += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(c)]
            elif c == '/':
                result += ' '

    return result.rstrip()