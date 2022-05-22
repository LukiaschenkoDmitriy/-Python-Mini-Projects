def checkLen(string, word_len, ltype):
	if ltype == 'max':
		if len(str(string)) < word_len:
			return True
		return False

	if ltype == 'min':
		if len(str(string)) < word_len:
			return True
		return False
	return False


def uncodingNum(coding_num, output = False, min_len = 6, max_len = 16):
	coding_num = int(coding_num)
	hoverList = []

	for i in range(1,coding_num):
		step = coding_num/i
		if checkLen(int(step), max_len, 'max'):
			if float(step) - int(step) == 0:
				hoverList.append(int(step))
				if output:
					print(int(step))

		if checkLen(int(step), min_len, 'min'):
			break

	return hoverList



