#!/usr/bin/env python

import os
import re
import unicodedata
import codecs
from io import open
import itertools
import csv

#Function to extract sentence/response pairs for a specified character
def loadLinePairs(filename, character, fields, character_lines):
	lines = []
	linePairs = []
	#Read all lines from transcript file
	with open(filename, 'r') as f:
		for line1 in f:
			if ":" in line1 == False:
				continue
			values1 = line1.split(":")
			lineObj1 = {}
			if len(values1) < 2:
				continue
			for i, field in enumerate(fields):
				lineObj1[field] = values1[i]
			lines.append(lineObj1)
	
	#Parse specified character responses from file and format
	for i in range(len(lines) - 1):
		firstLine = lines[i]
		firstChar = firstLine["characterID"].strip()
		firstText = firstLine["text"].strip()
			
		secondLine = lines[i+1]
		secondChar = secondLine["characterID"].strip()
		secondText = secondLine["text"].strip()
			
		if secondChar == character or secondChar == "Squidward Tentacles":
			firstText = re.sub("\n", "", firstText)
			firstText = re.sub("[\[].*?[\]]", "", firstText)
			secondText = re.sub("[\[].*?[\]]", "", secondText)
			linePairs.append([firstText, secondText])

	delimiter = '\t'
	# Unescape the delimiter
	delimiter = str(codecs.decode(delimiter, "unicode_escape"))
	
	#rite sentence response pairs to csv file
	with open(character_lines, 'w') as f:
		writer = csv.writer(f, delimiter=delimiter, lineterminator='\n')
		for pair in linePairs:				
			writer.writerow(pair)
	
	print(linePairs)
	


def printLines(file, n=10):
    with open(file, 'rb') as datafile:
        lines = datafile.readlines()
    for line in lines[:n]:
        print(line)



FIELDS = ["characterID", "text"]
filename = os.path.join("sample_transcript.txt")
loadLinePairs(filename, "Squidward", FIELDS, "squid_linePairs.txt")
printLines("squid_linePairs.txt")