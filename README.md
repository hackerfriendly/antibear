antibear.py
===========

Simple Alphabear (Boggle, Scrabble, etc.) solver

For word games like Alphabear, where you gain points for making long words
out of a constrained selection of letters.

https://play.google.com/store/apps/details?id=com.spryfox.alphabear&hl=en

Give it all of the letters on the board in any order. It returns a list of
all words that can be spelled with them along with the word length, longest
words last.

Usage:

	./alphabear.py [all of the letters on the board]

Example: 

	./alphabear.py ealsbuhibubateihtdhs
	...
	10 healthiest
	10 stubbliest
	10 subtleties
	11 debilitates
	11 established

To find a word with a specific letter in it (eg. the red letters) just grep
for them:

	./antibear.py edvdudssdatphatiihiigt |grep h

Will only work on systems with python, awk, grep, and /usr/share/dict/words
(eg. Linux and Mac OS X).

The quality of the words you get depends greatly on the quality of your
words file.

Enjoy!

--Rob
