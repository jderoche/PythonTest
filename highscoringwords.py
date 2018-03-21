__author__ = 'codesse'


class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        self.leaderboard = []  # initialise an empty leaderboard
        with open(validwords) as f:
            self.valid_words = f.read().splitlines()

        with open(lettervalues) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
        :return:
        """
        wordvaluelist = {} # prepare datadict for leaderboard
        maxscore = 0       # preparre value for maxscore

        # build the datadict with all the word and score
        for word in self.valid_words:
            computescore = self.ComputeWordScore(word)
            if (maxscore<computescore):     #get the hight score
                maxscore = computescore
            wordvaluelist[str(word)] = int(computescore)
        numberofleader = 0
        self.leaderboard=[]
        for score in range(maxscore,0,-1):
            for key, val in wordvaluelist.items():
                if (val >= score):
                    if key in self.leaderboard:
                        continue
                    else:
                        self.leaderboard.append(key)
                        #print("Word:%s : %d" %(key,val))
                    numberofleader = numberofleader +1
                if (numberofleader>=self.MAX_LEADERBOARD_LENGTH):
                    break
            if (numberofleader>=self.MAX_LEADERBOARD_LENGTH):
                break

    def build_leaderboard_for_letters(self, starting_letters):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.
        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return:
        """
        charindex=0
        newlist=[]
        # to find all valid word according to the starting_letters
        c = starting_letters[0]
        for word in self.valid_words:
            if (c == word[0]): #found
                newlist.append(word)
        for charindex in range(0,len(starting_letters)):
            self.FindByWordFromList(starting_letters,charindex,newlist)

        wordvaluelist = {} # prepare datadict for leaderboard
        maxscore = 0       # preparre value for maxscore

        # build the datadict with all the word and score
        for word in newlist:
            computescore = self.ComputeWordScore(word)
            if (maxscore<computescore):     #get the hight score
                maxscore = computescore
            wordvaluelist[str(word)] = int(computescore)
        numberofleader = 0
        self.leaderboard=[]
        for score in range(maxscore,0,-1):
            for key, val in wordvaluelist.items():
                if (val >= score):
                    if key in self.leaderboard:
                        continue
                    else:
                        self.leaderboard.append(key)
                        #print("Word:%s : %d" %(key,val))
                    numberofleader = numberofleader +1
                if (numberofleader>=self.MAX_LEADERBOARD_LENGTH):
                    break
            if (numberofleader>=self.MAX_LEADERBOARD_LENGTH):
                break

    def FindByWordFromList(self, currentword,charindex,newlist):
        c = currentword[charindex]
        count =  len(newlist)
        extractlist = []
        index = 0
        # to find the next valid word with the required char
        while (count>0):
            word = newlist[index]
            if (charindex<len(word)): #if word is long enough
                if (c != word[charindex]): # not match remove it
                    newlist.remove(word)
                else:
                    index = index +1
            else:
                newlist.remove(word)  #if too shot remove it
            count=count-1

    def ComputeWordScore(self,word):
        value = 0;
        # to find the next valid word with the required char
        for c in word:
            value = value + self.letter_values[c]
        return value