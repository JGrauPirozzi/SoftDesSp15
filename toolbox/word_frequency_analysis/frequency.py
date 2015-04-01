""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from collections import Counter

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	file = open(file_name,'r')
	lines = file.readlines()
	file.close()

	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]

	book = ''.join(lines).lower()
	remove = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
	for i in range(0,len(remove)):
		book = book.replace(remove[i],"")

	word_list = list(book.split())

	return word_list

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	count = Counter(word_list)
	
	rank = count.most_common(n)

	return rank

if __name__ == '__main__':
    #print(get_word_list('ec.txt'))
	print(get_top_n_words(get_word_list('ec.txt'), 100))
