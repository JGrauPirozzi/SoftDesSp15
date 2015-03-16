""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""
	#There is two options or is a new count or there is a count for that file.
	#First
	if reset == True and exists(file_name) ==  False:

		file = open(file_name, 'w+') #Create the file
		count = 1 #Set to 1
		file.write(count) #Write the count (1 Always)
		file.closed #Close the file
	#Second
	if reset == False and exists(file_name) == True:
		file = load(open(file_name, 'r+')) #Read the file
		file = 1 + file #Add to the count
		dump(file, open(file_name,'r+')) #Write the new count
		file.closed #Close the file

	return load(open(file_name,'r+')) #Return count for the file

if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))
