import random, sys
print('rock,paper,scissors')
#variables set
wins = 0
losses = 0
draws = 0
#while true loop for game
while True:
    print('%s Wins, %s Losses, %s draws' % (wins, losses, draws))#gets wins losses and ties based on strings of the same name
    while True: #loop for player input
        print('Enter your move: r for rock, p for paper, or s for scissors, q can be used to quit the game')
        playerMove = input()
        if playerMove =='q':
            sys.exit() #quits program
        if playerMove == 'r' or playerMove == 's' or playerMove == 'p':# sets player input possibilities
            break
        print('type r, p, s, or q')# player moves
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    randomNumber = random.randint(1,3)# random integer so the computer can pick their move
    if randomNumber == 1:#computer moves
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('scissors')

    if playerMove == computerMove:# results + adding to the scoreboard
        print('it is a tie!')
        draws = draws + 1
    elif playerMove == 'r' and computerMove == 's':
        print('you win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('you win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('you win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('you lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('you lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('you lose!')
        losses = losses + 1
