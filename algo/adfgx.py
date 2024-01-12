import random

def run(message, key, encrypt):
	"""Encrypt or decrypt a message using the ADFGVX cipher.

	:param message: the message to encrypt or decrypt
	:param key: the key to use to encrypt or decrypt
	:param encrypt: True to encrypt, False to decrypt
	:return: the encrypted or decrypted message
	"""
	alphabet = list('abcdefghiklmnopqrstuvwxyz')
	adfgx = list('ADFGX')

	# Randomize the alphabet based on the key
	random.seed(key)
	random.shuffle(alphabet)

	# Generate the ADFGX table
	table = []
	for i in range(5):
		table.append([0] * 5)
	for i in range(5):
		for j in range(5):
			table[i][j] = alphabet[i * 5 + j]
	
	if encrypt:
		# Replace j with i
		message = message.lower().replace('j', 'i')
		
		# Generate translation
		result = ''
		for c in message:
			for i in range(5):
				if c in table[i]:
					result += adfgx[i] + adfgx[table[i].index(c)]
					break
		
		result = list(key + result)

		# Generate permutation table
		p_table = []
		for i in range(len(key)):
			p_table.append([])

		i = 0
		while len(result) > 0:
			p_table[i].append(result.pop(0))
			i = (i + 1) % len(key)

		sorted_table = sorted(p_table, key=lambda x: x[0])

		# Generate the encrypted message
		final_result = ''
		for i in range(len(sorted_table)):
			for j in range(1, len(sorted_table[i])):
				final_result += sorted_table[i][j]
			final_result += ' 'if i < len(sorted_table) - 1 else ''

		return final_result
	else:
		s_key = sorted(list(key))
		message_list = message.upper().split(' ')

		# Generate permutation table
		p_table = []
		for i in range(len(key)):
			p_table.append([s_key[i], *list(message_list[i])])
		
		# Bring back the original order
		org_table = []
		for i in range(len(key)):
			for j in range(len(p_table)):
				if p_table[j][0] == key[i]:
					org_table.append(p_table[j][1:])
					break
		
		# Transpose the table
		org_table = list(map(list, zip(*org_table)))

		# Join the table
		join_table = ''
		for i in range(len(org_table)):
			join_table += ''.join(org_table[i])
		
		# Generate the decrypted message
		result = ''
		for i in range(0, len(join_table), 2):
			result += table[adfgx.index(join_table[i])][adfgx.index(join_table[i + 1])]

		return result
	