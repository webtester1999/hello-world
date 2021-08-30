#rockpaperscissor
print('welcome to rock paper scissor game')
print('i hope you know the rules already')
print('type the respective weapon to beat the opponent')
print('''
         rock
         paper
         scissor''')
R = 'rock'
P = 'paper'
S = 'scissor'


scores_a = 0
scores_b = 0
while scores_a !=10 and scores_b !=10:
    player_a = input('player A turn :')
    print("\n"*100)
    player_b = input('player B turn :')
    
    if player_a == R and player_b == P :
        print('player B wins')
        scores_b += 1
        print(f'''the scores are
                            player A scored {scores_a} points
                            player B scored {scores_b} points''')
    elif player_a == R and player_b == S :
        print('player B wins')
        scores_b += 1
        print(f'''the scores are
                            player A scored {scores_a} points
                            player B scored {scores_b} points''')
    elif player_a == P and player_b == R :
        print('player A wins')
        scores_a += 1
        print(f'''the scores are
                            player A scored {scores_a} points
                            player B scored {scores_b} points''')
    elif player_a == P and player_b == S :
        print('player B wins')
        scores_b += 1
        print(f'''the scores are
                            player A scored {scores_a} points
                            player B scored {scores_b} points''')
    elif player_a == S and player_b == R :
        print('player A wins')
        scores_a += 1
        print(f'''the scores are
                            player A scored {scores_a} points
                            player B scored {scores_b} points''')
    elif player_a == S and player_b == P :
        print('            player A wins')
        scores_a += 1
        print(f'''the scores are
                            player A scored {scores_a} points
                            player B scored {scores_b} points''')
    
    else:
        print('            this round tied')
        
if scores_a > scores_b:
    print('the player A wins the match ')
else:
    print('the player B wins the match')
