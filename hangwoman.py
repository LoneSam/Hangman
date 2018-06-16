import random

def printHangman (guesses):
	print("\nYou have",guesses,"guesses remaining, Hangwoman.")


	if guesses == 6:
		print(
"""
You're just dangling there, but you haven't been touched... yet.
  ______
  \|     \|
  o     |
 -|-    |
 /*\\  	|
		|
	  -----
"""  
	  )
	
	if guesses == 5:
		print(
"""
She's lost an arm!
  ______
  |	    |
  o     |
 -|     |
 /*\\  	|
		|
	  -----
"""  
	  )
	  
	if guesses == 4:
		print(
"""
She's lost a leg!
  ______
  |	    |
  o     |
 -|     |
 /*  	|
		|
	  -----
"""  
	  )
	  
	if guesses == 3:
	  	print(
"""
There goes the other arm...
  ______
  |	    |
  o     |
  |     |
 /*  	|
		|
	  -----
"""  
	  )
	 
	if guesses == 2:
	  	print(
"""
Bushwacked..
  ______
  |	    |
  o     |
  |     |
 /  	|
		|
	  -----
"""  
	  )
	
	if guesses == 1:
	  	print(
"""
I don't know what good just a torso will do you, but at least you're still alive...
  ______
  |	    |
  o     |
  |     |
   	    |
		|
	  -----
"""  
	  )
	 
	if guesses == 0:
	  		print(
"""
That's the end of her story. She died. Nobody attended her funeral...
JK! I went with Remington.
:) <3
  ______
  |	    |
  0     |
        |
   	    |
		|
	  -----
"""  
	  )

def printLetters (word,elters):
	line = ''
	for letter in word:
		if letter not in elters:
			line += ' ' + letter + ' ' 
		else:
			line += ' _ '
	print (line + '\n')
	print (elters + '\n')

def printScreen (guesses,word,elters):
	printHangman(guesses)
	printLetters(word,elters)

def getWord (difficulty):
	with open('words.txt') as f:
		words = f.read().splitlines()
	f.close()
	word = 'no_words_available'
	
	#first check if a word of that length exists
	#if no words are long enough, return false
	isLongEnough = False
	for w in words:
		if len(w) == difficulty:
			isLongEnough = True
			continue
	if isLongEnough == False:
		return word
	
	while len(word) != difficulty:
		word = random.choice(words)

	return word
	

def main():
	print ('\nWelcome to Hangwoman v0.7!!!')
	inGame = True
	while inGame:
		guesses = 6
		difficulty = ''
		elters = "abcdefghijklmnopqrstuvwxyz"
		word = 'no_words_available'
		finished = False
		
		
		while word == 'no_words_available':
			try:
				difficulty = int(input ('Okay Hangwoman, how many characters can you guess before dying?\n'))
				if type(difficulty) == int:
					word = getWord(difficulty)
					#print (word)
					if word == 'no_words_available':
						print ("Are you trying to die?! Luckily, they don't make words that big. Pick a lower number.\n")
	
			except ValueError:
				print("\nEllie, if you want to play, you have to enter a number. (Numbers are the things you can count to.)")
			
		
		print ('\nYour life-taking word has been selected. Good luck, Hangwoman!')		
		
		while not finished:
			elguess = 'start'
			while(len(elguess) != 1):	
				elguess = input('Guess a letter: ').lower()
				if (elguess not in elters):
					print ('That is not an available letter.')
					elguess = 'retry'
				else:
					elters = elters.replace(elguess,'_')
					continue
				
				
			if elguess in word:
				print ('\n-----------------\nGood job Ellie!')
				printScreen(guesses, word, elters)
			else:
				print ('\n-----------------\n"You gonna die, fool!" says Mr. T')
				guesses = guesses - 1
				printScreen(guesses,word,elters)
			
			count = 0
			remDup = ''.join(set(word))
			for l in elters:
				if l in remDup:
					count = count + 1
				
			#print('count: ',count)
			#print('guesses : ',guesses)
			if (count == 0 or guesses == 0):
				finished = True
	
		
		if (guesses > 0):
			print ("You won!!!")
			print ("Congratulations! The word was '"+word+"'")
			print ('You live to fight another day, but probably not for long...')
		else:
			print ('It would suck to be you right now. I mean, if it were even possible for you to be anymore.')
			print ("The word was '" + word + "'")
			
		resp = ''
		while True:
			resp = input ('Would you like to play again? [y/n]: ').lower()
			print(resp)
		
			if resp == 'y':
				print ("\nRisky girl! Good luck. Remmy is rootin' for ya!")
				break
			elif resp == 'n':
				print ('That is probably a safe decision.\nGoodbye for now, Hangwoman.')
				exit()
		
main()
   