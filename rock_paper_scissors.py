import random

user_wins = 0
computer_win = 0

while True:
    user_input =input("Type Rock/Paper/Scissors or Q to quit:").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = radom.randint(0, 2)  
    #rock :0 ,paper:1, scissors:2
    
print("Goodbye!")