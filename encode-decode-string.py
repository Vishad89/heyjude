"""Given a string containing uppercase characters (A-Z), compress repeated 'runs' of the same character by storing the length of that run, and provide a function to reverse the compression. The output can be anything, as long as you can recreate the input with it.

Example:

Input: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
Output: 12W1B12W3B24W1B14W"""


from collections import defaultdict 

def encode(input_string):
	char_count = defaultdict(int)

	for char in input_string:
		char_count[char] +=1
	print char_count

	sum_ac = int(char_count['a']) + int(char_count['c']) 
	sum_bd = int(char_count['b']) + int(char_count['d'])

	if (sum_ac == sum_bd):
		print "equal ac & bd"
	elif (sum_ac > sum_bd):
		print "ac won the match"
	else:
		print "bd won the match"


yourstring = raw_input("input your string here: ")
encode(yourstring)