import random

def rps():
    choices = ['rock', 'paper', 'scissors']
    player = None
    rounds = 3
    cpoints = 0
    ppoints = 0

    print("Welcome to rock, paper, scissors")
    while rounds > 0 and (cpoints < 2 and ppoints < 2):
        
        print(f"There are {rounds} rounds remaining.")
        print(f"Your points: {ppoints}")
        print(f"Computer score: {cpoints}")  
   
        comp = random.choice(choices)
        player = input("rock, paper, or scissors?: ").strip().lower()
   
        if player not in choices:
            print("Invalid input. Type in 'rock', 'paper', or 'scissors'.")
            continue
 
        if player == 'rock':
            if comp == 'rock':
                print("You guys must be building a house together 😂")
            elif comp == 'paper':
                print("You've been covered up!")
                cpoints += 1  
            else:
                print("You've crushed the competition!")
                ppoints += 1
        
        elif player == 'paper':
            if comp == 'rock':
                print("You've wrapped up the competition!")
                ppoints += 1
            elif comp == 'paper':
                print("Y'all must be making confetti😂")    
            else:
                print("You've been shredded!")
                cpoints += 1 
        
        else:  
            if comp == 'rock':
                print("You've been crushed!")
                cpoints += 1 
            elif comp == 'paper':
                print("You've shredded the competition!")  
                ppoints += 1  
            else:
                print("Must've opted to sharpen each other😂")
    
        rounds -= 1
        print(f"Your points: {ppoints}")
        print(f"Computer score: {cpoints}") 
          
    if ppoints == 2 or ppoints>cpoints:
        print("Congratulations! You've won 🎉")  
        print(f"Your points: {ppoints}")
        print(f"Computer score: {cpoints}")
    elif cpoints == 2 or cpoints>ppoints:
        print("Computer wins! Guess you're the bot now 😂")
        print(f"Your points: {ppoints}")
        print(f"Computer score: {cpoints}")
    else:
        print("It's a tie!")  
        print(f"Your points: {ppoints}")
        print(f"Computer score: {cpoints}")

rps()
