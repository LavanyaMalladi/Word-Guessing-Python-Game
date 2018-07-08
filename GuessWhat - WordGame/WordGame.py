from random import randint
import sqlite3
def word_update(word, letters_guessed): 
    masked_word = ""
    for letter in word:
        if letter in letters_guessed:
            masked_word += letter
        else: masked_word += "-"
    print( "The word:", masked_word)

rand=randint(10,19)
#import sqlite3
conn=sqlite3.connect('lav.db')
print("OPENED")
cursor=conn.execute("SELECT * from names")
#for row in cursor:
#    print (row[1])
row=cursor.fetchall()
word=""
word=(','.join(row[rand]))
#print(word)
print("Welcome to GUESS WHAT! ")
print("Let's play!")
print("="*32)
print("IT'S A SPORT")
print("These are the no. of letters")
print(len(word))
print("_ "*len(word))


#print(row[1])
conn.close()
guesses = 5
# You can change this; it's how many letter guesses the user gets
print("You get 5 guesses")
letters_guessed = []
 
print ("="*32)
#print ("You get to guess %d letters." )% (guesses)
#print ("There are %s letters in the word.") % (len(word))
#print ("="*32)
 
while guesses != 0:
    letter = input("Enter a letter: ").lower()
    # Doesn't use up a guess if the user has already guessed that letter
    if letter in letters_guessed:
        print ("You already guessed that letter.")
    else:
        guesses = guesses - 1
        #print ("You have %d guesses left.") % (guesses)
        letters_guessed.append(letter)
    word_update(word, letters_guessed)
word_guesses = 1 # number of guesses to guess the word
word_guess = 0 # current guess number
if word_guesses == 1:
    print ("You get 1 guess to guess the word.")
else:
    print ("You get %d guesses to guess the word.") % (word_guesses)
while word_guess != word_guesses:
    guess = input("Guess the word: ").lower()
    if guess ==  word:
        print ("Congratulations") 
        break
    else:
        print ("Nope.")
    word_guess += 1
    if  word_guess == word_guesses:
        #print ("You ran out of tries!\nThe word was %s.") % (word)
        print(word + " IS THE ANSWER")
 
print ("\nThanks for playing Word Guess Game.")
