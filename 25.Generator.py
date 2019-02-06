# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25, 2019
File: Generator.py

Generates and displays sentences using simple gramma
and vocabulary. Words are chosen at random.

@author: Byen23
"""

# Request
"""Write a program that generates sentences."""

# Analysts
"""Sentences in any language have a structure defined by a grammar. They also include a set of words from the vocabulary of the language. The vocabulary of a language like English consists of many thousands of words, and the grammar rules are quite complex. For the sake of simplicity our program will generate sentences from a simplified subset of English. The vocabulary will consist of sample words from several parts of speech, including nouns, verbs, articales, and prepositions. From these words, you can build noun phrases, prepositional phrases, and verb phrases. From these constituent phrases, you can build sentences. FOr example, the sentence "The girl hit-the ball with the bat" contains three noun phrases, one verb phrase, and one prepositional phrase."""

"""
Phrase: Sentence, Noun phrase, Verb Phrase, Prepositional phrase.   
Its Constituents: Noun phrase + Verb Phrase, Article + Noun
		          Verb + Noun phrase + Prepositional phrase
				  Prepositional + Noun phrase.	           
"""
"""
The rule for Noun phrase says that is an Article is followed by (+) a Noun. Thus, a possible noun phrase is "the bat." Note that some of the phrases in the left column of Table 5-3 also appear in the right columns as contituents of other phrases. Although this grammar is much simpler than the complete set of rules for English grammar, you should still be able to generate sentences with quite a bit of structure.

The program will prompt the user for the number of sentences to generate. The proposed user interface follows:
	
	Enter the number of sentences: 3 
Outputs-->	THE BOY HIT THE BAT WITH A BOY
Outputs--> 	THE BOY HIT THE BALL BY A BAT
Outputs--> 	THE BOY SAW THE GIRL WITH THE GIRL
	
	Enter the number of sentences: 2
Outputs--> 	A BALL HIT A GIRL WITH THE BAT
Outputs--> 	A GIRL SAW THE BAT BY A BOY
"""
# Design 
"""
Of the many ways to solve the problem in this case study, perhaps the simplest is to assign the task of generating each phrase to a separate function. Each function builds, and returns a string that represents its phrase. This string contains words drawn from the parts of speech and from other phrases. When a function needs an individual word, it is selected at random from the words in that part of speech. When a function needs another phrase, it calls another function to build that phrase. The results, all strings, are concatenated with spaces and returned.

The function for Sentences is the easiest. It just calls the function for Noun phrase and Verb phrase and concatenate the results, as in the following:
"""
# Implementation (Coding)
"""When function use a common pool of datam you should define or initialize the data before the function are defined. Thus, the variables for the data are intialized just below the import statement."""

import random

# Vocabulary words in 4 different parts of speech
articles 		= ("A", "THE")
nouns 			= ("BOY", "GIRL", "BAT", "BALL")
verbs 			= ("HIT", "SAW", "LIKED")
prepositions 	= ("WITH", "BY")

def sentence():
	"""Builds and returns a sentence."""
	return nounPhrase() + " " + verbPhrase()

"""The function for Noun phrase picks an article and a noun at random from the vocabulary, concatenates them, and returns the result. We assume that the variables articles and nouns refer to collections of these parts of speech and develop these later in the design. The function random.choice returns a random element from such a collection."""

def nounPhrase():
	"""Builds and returns a noun phrase."""
	return random.choice(articles) + " " + random.choice(nouns)

"""The design of the remaining two phrase structure function is similiar.
The main funciton drives the program with a count-controlled loop:"""

def verbPhrase():
	"""Builds and returns a noun phrase."""
	return random.choice(articles) + " " + nounPhrase() + " " + 	 		   prepositionalPhrase()
		   
def prepositionalPhrase():
	"""Builds and reutnrs a prepositional phrase."""
	return random.choice(prepositions) + " " + nounPhrase()
		          
def main():
	"""Allows the user to input the number of sentences to generate."""
	number = int(input("Enter the number of sentences: "))
	for count in range(number):
		print(sentence())

# The entry point for program execution
if __name__ == "__main__":
	main()
	