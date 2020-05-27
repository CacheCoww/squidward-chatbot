#!/usr/bin/env python
"""
File to parse the transcript file for specified character's lines in preparation for generating data to feed to the RNN models. 

"""

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

		#Adding all character dialog lines to aid in training
		#Remove this line to only train with specified character's lines
		firstText = re.sub("\n", "", firstText)
		firstText = re.sub("[\[].*?[\]]", "", firstText).strip()
		secondText = re.sub("[\[].*?[\]]", "", secondText).strip()
		linePairs.append([firstText, secondText])

		#Append Squidward (or specified character) lines
		if secondChar == character or secondChar == "Squidward Tentacles":
			firstText = re.sub("\n", "", firstText)
			firstText = re.sub("[\[].*?[\]]", "", firstText).strip()
			secondText = re.sub("[\[].*?[\]]", "", secondText).strip()
			linePairs.append([firstText, secondText])

	delimiter = '\t'
	# Unescape the delimiter
	delimiter = str(codecs.decode(delimiter, "unicode_escape"))
	
	#rite sentence response pairs to csv file
	with open(character_lines, 'w') as f:
		writer = csv.writer(f, delimiter=delimiter, lineterminator='\n')
		for pair in linePairs:				
			writer.writerow(pair)

	
def printLines(file, n=10):
    with open(file, 'rb') as datafile:
        lines = datafile.readlines()
    for line in lines[:n]:
        print(line)


#Main function to call the other functions and save sentence-response pairs in squid_linePairs.txt file
def main():
	FIELDS = ["characterID", "text"]
	filename = os.path.join("compiled_transcripts.txt")

	loadLinePairs(filename, "Squidward", FIELDS, "squid_linePairs.txt")
	printLines("squid_linePairs.txt")

if __name__ == "__main__":
	main()