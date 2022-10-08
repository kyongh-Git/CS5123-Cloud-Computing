#!/usr/bin/python3
import os
import sys
import re

# Stop words list
stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
# regular expression
regex = re.compile('[^a-zA-Z]')
# input comes from STDIN (standard input)
for line in sys.stdin:
    # line is a line from the file input. EXAMPLE line: I love Oklahoma
	# remove leading and trailing whitespace
	line = line.strip()
	# convert UPPERCASES to LOWERCASES
	line = line.lower()
	# split the line into words
	words = line.split()
	# increase counters
	wordCounter = 0
	for word in words:
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the Reduce step, the input for reducer.py
		# tab-delimited; the trivial word count is 1
		# remove non alphabetical characters
		temp = regex.sub('', word)
		if temp not in stop_words and temp != '':
			wordCounter += 1
			
	# file path
	filepath = os.environ["map_input_file"]
	filename = os.path.split(filepath)[-1]
	filename = filename.split(".")[0]
	# (filename, number of words in line)
	print('%s\t%s' % (filename, wordCounter))