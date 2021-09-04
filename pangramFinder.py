#!/usr/bin/env python3

"""Script gets pangrams for an input word.
Args:
search word: character string to search

Example Usage:
$ python pangramFinder.py <search word>

Example Input and Output:
$ python pangramFinder.py cogzila
> ['pangramFinder.py', 'cogzila']
> zoological
"""

import sys

def makeset(word):
	'''Return a sorted string of unique characters from the input string
	'''
	return "".join([i for i in set(sorted(word))])

def findPangrams(searchword,spellingbeedict):
	'''Search spellingbeedict for input characters.
	Outputs message if no pangrams are found.
	'''
	return spellingbeedict.get(makeset(searchword),['Search did not return any pangrams.'])

def createDictionary(numletters,inputdictionary="words_alpha.txt"):
	#create empty dictionary to store pangrams
	spellingbeedict={}
	#read in input dictionary
	with open(inputdictionary,"r") as f:
		#read in dictionary of words by line
		for word in f.readlines():
			#strip newline character
			word=word.strip()
			#store string of sorted unique letters
			wordset=makeset(word)
			#store pangrams in spellingbee dict
			if wordset in spellingbeedict:
				spellingbeedict[wordset].append(word)
			else:
				spellingbeedict[wordset]=[word]
	return spellingbeedict

def main():
	#store input word as searchword
	searchword=sys.argv[1].lower()
	#save list of pangrams to pangramlist
	pangramlist=findPangrams(searchword,createDictionary(numletters=len(set(searchword))))
	#print pangrams separated by newlines
	print("\n".join(pangramlist))

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 2:
        main()
    else:
        sys.stderr.write("Error: Invalid number of parameters\n")
        print(__doc__)
        sys.exit(1)