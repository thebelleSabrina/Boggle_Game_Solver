"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	start = time.time()
	lst = []
	lst = read_dictionary(lst)
	total = []
	word_num = []
	str_lst = []
	use_index = []
	for i in range(1, 5):
		char = input(f'{i} row of letters: ').lower()
		letter = ''
		for each in char:
			if each.isalpha():  # delete space in the input
				letter += each
		if letter.isalpha and len(letter) != 4:  # constraint the length and content of input
			print('Illegal input')
			break
		word = []
		for each in letter:
			if letter.isalpha():
				word.append(each)
		total.append(word)
	for x in range(len(total)):  # row
		for y in range(len(total[0])):  # column
			char = total[x][y]  # gets the first character
			word_num.append(char)
			use_index.append((x, y))
			finds(word_num, x, y, total, lst, str_lst, use_index)
			word_num = []  # clear the original word_num for next character
			use_index = []
	print(f"There are {len(str_lst)} words in total.")
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def finds(word_num, x, y, total, lst, str_lst, use_index):
	if len(word_num) >= 4:
		ans = ''
		for i in word_num:   # turns list into string
			ans += i
		if ans in lst and ans not in str_lst:
			print(f'Found "{ans}"')
			str_lst.append(ans)
	for j in range(-1, 2, 1):    # get the first character's neighbor
		for k in range(-1, 2, 1):
			if 0 <= x + j < 4:  # check if the character is within the boggle board
				if 0 <= y + k < 4:
					new_char = total[x + j][y + k]
					if (x+j, y+k) not in use_index:  # avoids the same character appear in the same location
						check_lst = ''
						for each in word_num:
							check_lst += each
						if has_prefix(check_lst, lst):  # makes the code run faster through the new function
							# choose
							use_index.append((x+j, y+k))   # list for index
							word_num.append(new_char)  # list for character
							# explore
							finds(word_num, x+j, y+k, total, lst, str_lst, use_index)
							# un-choose
							use_index.pop()
							word_num.pop()


def read_dictionary(lst):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip('\n')
			lst.append(word)
	return lst


def has_prefix(sub_s, lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	vocab_list = lst
	for vocab in vocab_list:
		if vocab.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
