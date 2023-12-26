import random

def get_choices():
    options = ['ROCK', 'PAPER', 'SCISSORS']
    while True:
        player_choice = input("🔘 Enter rock/paper/scissors: ").upper()
        if player_choice in options: break
        elif player_choice == 'STOP': return None        
        else: print("🔺 Enter a valid input.")
        
    computer_choice = random.choice(options)
    choices = {'player':player_choice, 'computer': computer_choice}
    return choices

def play(player, computer):
    global player_score, comp_score  
    print(f"🔹 You chose {player} || Computer chose {computer}.")
    if player == computer: player_score += 1 ; comp_score += 1
    elif (player,computer) == ("ROCK",'SCISSORS') or ('PAPER','ROCK') or ('SCISSORS','PAPER'): player_score += 1
    else: comp_score += 1

def result(player_score, comp_score):
    if player_score>comp_score: print("🥳 Player wins!!!")
    elif player_score<comp_score: print("🎭 Player lost :(")
    else: print("📣 It's a Tie!")

print("---------WELCOME TO ROCK🪨 PAPER📄 SCISSORS✂️ GAME---------")
print("🔸 Enter 'stop' to end the game.")
player_score = 0
comp_score = 0
while True:
    choices = get_choices()
    if choices==None: result(player_score,comp_score) ; break
    play(choices['player'],choices['computer'])
    print(f"👦 Player Score: {player_score} \n🤖 Computer Score: {comp_score}")