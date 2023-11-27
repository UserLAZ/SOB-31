import random

def compare_numbers(number, user_guess):
    ## your code here
    cowbullcount = [0, 0] # list that that saves number of cows in index 0. Same thing for bulls but in index 1
    number_str = str(number) # changes int value to str and creates a variable taht checks for simillarity in digits
    user_guess_str = str(user_guess)
    user_guess_str = str(user_guess)
    for i in range(4):
        #A loop that double-checks simillarity in digits
        if user_guess_str[i] == number_str[i]:
            cowbullcount[1] +=1 # puts a 1 to the bull index[1]

        elif user_guess_str[i] in number_str:
            cowbullcount[0] +=1 #puts/adds 1 to cow index[0]
    return cowbullcount
   

playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
guesses = 0
print (number)

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    #replace raw with parenthesis
    user_guess = input("Give me your best guess! ")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
