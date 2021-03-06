"""
Scrabble™ is a long established and popular word game in many different languages.

The object of the game is to build valid words (for this exercise words are valid if they are present in the wordlist.txt file
supplied) from a set of letter (tiles) that the player holds.

Each letter carries a different score value based on its frequency in the language. For example in English vowels
such as A and E score only 1 point but less frequent letters such as K and J score 5 and 8 points respectively. The
score for any particular word is the sum of the values of all the letters that make up the word. So for example:
the word cabbage scores C3 + A1 + B3 + B3 + A1 + G2 + E1 = 14 points. The score values of letters in English are shown
in the letterValues.txt file.

The objective of this coding challenge is twofold:
(1) to create a leaderboard of the 100 highest scoring words in English based on the words in the wordlist.txt file.
Words should be ordered in descending order with the highest scoring first. If several words have the same score they
should be ordered alphabetically.
(2) to identify all the valid words that can be created from a supplied starting String of random letters. The length
of the random starting String may vary but could be assumed to be in the range of 5-15 characters. Again, words should
be ordered in descending order with the highest scoring first. If several words have the same score they should be
ordered alphabetically.

Some skeleton Python code is provided for the exercise. Please use the code provided but do not change it. Create
additional code as required. A HighScoringWords class with two unimplemented functions matching the numbered objectives
above is in the file highscoringwords.py
(1) def build_leaderboard_for_word_list(self):
(2) def build_leaderboard_for_letters(self, starting_letters):
Add your code to the highscoringwords.py file but do NOT change or remove the provided code.

Although writing code to assemble the correct leaderboards is the highest priority, your code may also be benchmarked
for performance.

YOUR CODE SHOULD THEREFORE BE OF PRODUCTION QUALITY
"""

"""
This class provide service to reorder a list of word
using alphabetically

"""
import highscoringwords


"""function to loock for a valid word having the last valid word with the next
char and next char position
"""
def ComputeWordScore(word):
    global highScore
    value = 0;
    # to find the next valid word with the required char
    for c in word:
        value = value + highScore.letter_values[c]
    print("Value of %s is %d" %(word, value))
    return value

##def FindWordListFromFirstChar(currentword):
##    global highScore
##    found = 0;
##    charindex=0
##    newlist=[]
##    # to find all valid word according to the currentword
##    c = currentword[0]
##    for word in highScore.valid_words:
##        if (c == word[0]): #found
##            newlist.append(word)
##    for charindex in range(0,len(currentword)):
##        FindByWordFromList(currentword,charindex,newlist)
##    return newlist
##
##def FindByWordFromList(currentword,charindex,newlist):
##    global highScore
##    c = currentword[charindex]
##    count =  len(newlist)
##    extractlist = []
##    index = 0
##    # to find the next valid word with the required char
##    while (count>0):
##        word = newlist[index]
##        if (charindex<len(word)): #if word is long enough
##            if (c != word[charindex]): # not match remove it
##                newlist.remove(word)
##            else:
##                index = index +1
##        else:
##            newlist.remove(word)  #if too shot remove it
##        count=count-1

#for TEST function
highScore = highscoringwords.HighScoringWords()
highScore.build_leaderboard_for_word_list()

highScore.build_leaderboard_for_letters("air")







