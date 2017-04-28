"""
Simple Hangman
If you want to win the game, you have to give the input by letter,
if you give more than on letter it will count as an attempt, and
take one life from the 5. It will take as input any ASCII char,
so input the right letters if you want to win the game.
If you guess the letter in the word, the attempts variable does
not increase, after you guess every letter, you won the game.
"""
# TODO use regex automatically get words from a webpage

word = "pingpongpongping"

#create the guessing word
guess_word = "?" *(len(word))

attempts = 0
while attempts < 5:
  print('\n')
  print(guess_word)
  letter = input('Guess a letter = ')
  while(len(letter) != 1):
    print('Only a letter allowed')
    attempts += 1
    print('You have ', str(5-attempts), ' lives left')
    letter = input('Guess a letter = ')
  answer = [x for x, i in enumerate(word) if i == letter]
  if answer == []:
    attempts += 1
    print('Letter is not in the word')
    print('You have ', str(5-attempts), ' lives left')
  else:
    for i in answer:
      guess_word = guess_word[:i] + letter + guess_word[i+1:]
  if ('?' not in guess_word):
    print("Congrats!")
    quit()

if (attempts == 5):
  print('You have lost!')


