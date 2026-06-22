# this is a game of rock paper scissors
import random

def swg(a,b): # a is always the player, b is the bot
    if a == b:
        print("its a drawww")
    elif a == "stone" and b == "scissors":
        print("Player wins!!!!")
    elif a == "stone" and b == "paper":
        print("you lose, losser LLLLLLLL")
    elif a == "scissors" and b == "stone":
        print("you lose, losser LLLLLLLL")
    elif a == "scissors" and b == "paper":
        print("Player wins!!!!")
    elif a == "paper" and b == "scissors":
        print("you lose, losser LLLLLLLL")
    elif a == "paper" and b == "stone":
        print("Player wins!!!!")
    else:
        print("what are you doing play properlyyyyy")
    
a=["stone","scissors","paper"]

bot = random.choice(a).lower().strip()
player = input("stone\nscissors\npaper\nShoot: ").lower().strip()
print(f"bot chooses {bot}")
swg(player,bot)

print ("now the game has ended by 😁✌️")