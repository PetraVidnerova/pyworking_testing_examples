import random

def is_valid_play(play):
    return play in ["rock", "paper", "scissors"]

def random_play():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_game_result(human, computer):
    if human  == computer:
        return 'tie'
    elif (human, computer) in [ ('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]:
        return 'human'
    else:
        return 'computer'

def main(input=input):
    human = ''
    while not is_valid_play(human):
        human = input('rock, paper, or scissors?')

    computer = random_play()

    print(computer)

    res =  determine_game_result(human, computer)
    if res == 'tie':
        print("It's a tie!")
    else:
        print(res, "wins")
    

if __name__ == "__main__":
    main()
        
