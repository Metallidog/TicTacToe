from random import randint

play_game = True  #Let's play this thing
turn, value = 'X', -1   #Someone has to start
game_grid = [[0 for x in range(3)] for y in range(3)]
             
row_matrix=[((0,0),(0,1),(0,2)),
            ((1,0),(1,1),(1,2)),
            ((2,0),(2,1),(2,2)),
            ((0,0),(1,1),(2,2)),
            ((0,0),(1,0),(2,0)),
            ((1,0),(1,1),(1,2)),
            ((2,0),(2,1),(2,2)),
            ((0,2),(1,1),(2,0))]

def print_progress():
    for r in game_grid:
        for c in r:
            print ['.','O','X'][c],
        print
    print
    
def check_game():
    unplayed_box = False #flag to continue playing
    for r in row_matrix:
        total = 0
        for c in r:  
            val = game_grid[c[0]][c[1]]
            if not val: unplayed_box = True 
            total += val
            if abs(total) == 3: return (False, total)
    return (True, total) if unplayed_box else (False, total)

def random_game(turn, value, found=False):
    while not found: #looking for an empty square
        c, r = randint(0,2), randint(0,2)
        if not game_grid[r][c]: game_grid[r][c], found = value, True
    return ('O',1) if turn == 'X' else ('X',-1)


while play_game:
    turn, value = random_game(turn, value)
    play_game, winner = check_game()
    print_progress()    


if abs(winner)==3: print 'Winner is {}'.format(('X','O')[winner>0])
else: print 'Tie'
