from num2words import num2words

def run(param):
    message, key, encrypt = param['message'], param['key'], param['encrypt']
    message_list = list(message.replace(' ', '').replace('j', 'i').lower())

    try:
        key = int(key)
        
        numeric = list(str(key))
        
        key = num2words(key)
        key = key.replace('-', '')
    except:
        raise Exception('Key must be an integer.')

    alphabet1 = list('abcdefghiklmnopqrstuvwxyz')

    grid1 = []
    for i in range(5):
        for j in range(5):
            grid1.append(alphabet1[j * 5 + i])

    alphabet2 = []
    for c in key + 'abcdefghiklmnopqrstuvwxyz':
        if c not in alphabet2 and c != 'j':
            alphabet2.append(c)

    grid2 = []
    for i in range(25):
        grid2.append(alphabet2[i])

    idx = 0
    segment = []
    while len(message_list) > 0:
        s_word = ''
        for i in range(int(numeric[idx])):
            if len(message_list) == 0:
                break
            s_word += message_list.pop(0)
        idx = (idx + 1) % len(numeric)
        segment.append(s_word[::-1])

    if not encrypt:
        grid1, grid2 = grid2, grid1

    result = ''
    for s in segment:
        for c in s:
            result += grid1[grid2.index(c)]
        
    return result
