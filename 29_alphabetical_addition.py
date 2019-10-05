'''
Alphabetical Addition

('a', 'b', 'c') --> 'f'
('a', 'b') --> 'c'
('z') --> 'z'
('y', 'c', 'b') --> 'd'
() --> 'z'
'''

import string

def add_letters(*letters):

	if len(letters) > 0:
		alphabet_dict = dict(zip(string.ascii_lowercase, range(1, 27)))
		add_sum = sum([alphabet_dict[x] for x in letters])

		if add_sum>26:
			remainder = divmod(add_sum, 26)[1]

			if remainder == 0:
				return 'z'
			else:
				return [k for k, v in alphabet_dict.items() if v == remainder][0]
		else:
			return [k for k, v in alphabet_dict.items() if v == add_sum][0]
	else:
		return 'z'

