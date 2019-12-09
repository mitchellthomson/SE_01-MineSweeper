#MineSweep Exercise 2
import random

board = []

#generate the board, so theres not too many mines generate a number from 0-3, 3's will become mines everything else safe zones
i = 0
for x in range(16):
    z = random.randint(0,3)
    z = str(z)
    board.append(z)

i = 0
while i < len(board):
    if board[i]=='3':
        board[i]='*'
    else:
        board[i]='.'
    i = i + 1

#print('Here is the Random Board')
#print(board[0:4])
#print(board[4:8])
#print(board[8:12])
#print(board[12:16])
#print('\n')

#board = [0, '*', 0, 0, 0, 0, 0, '*', 0]
boundary = [9,9,9,9,9,9]
topRow = board[0:4]
topRow.insert(0,9)
topRow.append(9)
midRow = board[4:8]
midRow.insert(0,9)
midRow.append(9)
botRow = board[8:12]
botRow.insert(0,9)
botRow.append(9)
newbotRow = board[12:16]
newbotRow.insert(0,9)
newbotRow.append(9)

fullboard = [boundary,topRow,midRow,botRow,newbotRow,boundary]

#print(fullboard)
count = 0
x = 1
y = 1
play = fullboard

while x < 5:
    count = 0
    y = 1
    while y<5:
        count = 0
        cur = play[x][y]
        if cur != '*':
            if play[x-1][y-1] == '*':
                count = count +1
            if play[x-1][y] == '*':
                count = count +1
            if play[x-1][y+1] == '*':
                count = count +1
            if play[x][y-1] == '*':
                count = count +1
            if play[x][y+1] == '*':
                count = count +1
            if play[x+1][y-1] == '*':
                count = count +1
            if play[x+1][y] == '*':
                count = count +1
            if play[x+1][y+1] == '*':
                count = count +1
            play[x][y]=count

        y = y + 1

    x = x +1

play[1].pop(0)
play[1].pop(4)
play[2].pop(0)
play[2].pop(4)
play[3].pop(0)
play[3].pop(4)
play[4].pop(0)
play[4].pop(4)
#print('Here is the Solution')
#print(play[1])
#print(play[2])
#print(play[3])
#print(play[4])
gameBoard = play[1:5]


displayBoardrow1 = ['.','.','.','.']
displayBoardrow2 = ['.','.','.','.']
displayBoardrow3 = ['.','.','.','.']
displayBoardrow4 = ['.','.','.','.']
displayBoard = [displayBoardrow1,displayBoardrow2,displayBoardrow3,displayBoardrow4]

gamestatus = True
i = 0
minecount = 0
while i<len(gameBoard):
    temp =gameBoard[i].count('*')
    minecount = minecount +temp
    i = i + 1
print(gameBoard)

print('Welcome to MineSweeper, Please input where you would like to click')
gameCounter = 16-minecount
while gamestatus == True:
    print('   ',0,'  ',1,'  ',2,'  ',3)
    print(0,displayBoardrow1)
    print(1,displayBoardrow2)
    print(2,displayBoardrow3)
    print(3,displayBoardrow4)

   
    locy = input('Input your X coordinate, Number Between 0 and 3: ')
    locx = input('Input your Y coordinate, Number Between 0 and 3: ')
    locy = int(locy)
    locx = int(locx)

    coords = gameBoard[locy][locx]
    displayBoard[locy][locx] = str(coords)

    if displayBoard[locy][locx] =='.':
        gameCounter = gameCounter - 1

    if coords == '*':
        print('    Hit a Mine GameOver')
        print('   ',0,'  ',1,'  ',2,'  ',3)
        print(0,displayBoardrow1)
        print(1,displayBoardrow2)
        print(2,displayBoardrow3)
        print(3,displayBoardrow4)
        gamestatus = False

    if coords ==0:
        if gameBoard[locy-1][locx] == 0 and locy!= 0:
            displayBoard[locy-1][locx] = str(coords)
        if gameBoard[locy+1][locx] == 0 and locy!=3:
            displayBoard[locy+1][locx] = str(coords)
        if gameBoard[locy][locx-1] == 0 and locx !=0:
            displayBoard[locy][locx-1] = str(coords)
        if gameBoard[locy][locx+1] == 0 and locx< 3:
            displayBoard[locy][locx+1] = str(coords)
 
    if gameCounter == 0:
        print('You Win!')
        print('   ',0,'  ',1,'  ',2,'  ',3)
        print(0,displayBoardrow1)
        print(1,displayBoardrow2)
        print(2,displayBoardrow3)
        print(3,displayBoardrow4)
        gamestatus = False