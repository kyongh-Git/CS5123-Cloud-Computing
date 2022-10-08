#!/usr/bin/python3
from operator import itemgetter
import sys

current_word = None
current_count = 0
current_num = 0
word = None

# input comes from STDIN
# NOTE: Reducer input is the mergerd and sorted output of the mapper
# The above input comes from multiple file input lines which contains multiple "I", "love", "loves", and "Oklahoma"
for line in sys.stdin:
	# remove leading and trailing whitespace
	# Similar to mapper, reducer also processes the input line by line from the intermediate mapper output
	line = line.strip()
	# parse the input we got from mapper.py
	word, count = line.split('\t', 1)#(Oklahoma,1)

	# convert count (currently a string) to int
	try:
		count = int(count)	
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue
	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	# The below statements increments the counter only if the word from "line" is the current_word
	# Else writes the current_word and its count along with updating the current_word
	if current_word == word:
		current_count += count
		current_num += 1
	else:
		if current_word:
			# write result to STDOUT
			# devide total count by number of lines to calculate average
			print('%s\t%s' % (current_word, current_count/current_num))
		current_count = count
		current_word = word
		# reset the line counter
		current_num = 0

# do not forget to output the last word if needed!
if current_word == word:
	# devide total count by number of lines to calculate average
	print('%s\t%s' % (current_word, current_count/current_num))