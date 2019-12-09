#MineSweep Exercise 1
import random

board = []

#generate the board, so theres not too many mines generate a number from 0-3, 3's will become mines everything else safe zones
i = 0
for x in range(9):
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

print('Here is the Random Board')
print(board[0:3])
print(board[3:6])
print(board[6:9])
print('\n')

#board = [0, '*', 0, 0, 0, 0, 0, '*', 0]
boundary = [9,9,9,9,9]
topRow = board[0:3]
topRow.insert(0,9)
topRow.append(9)
midRow = board[3:6]
midRow.insert(0,9)
midRow.append(9)
botRow = board[6:9]
botRow.insert(0,9)
botRow.append(9)
fullboard = [boundary,topRow,midRow,botRow,boundary]

#print(fullboard)
count = 0
x = 1
y = 1
play = fullboard

while x < 4:
    count = 0
    y = 1
    while y<4:
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

#print (play[1:4])

play[1].pop(0)
play[1].pop(3)
play[2].pop(0)
play[2].pop(3)
play[3].pop(0)
play[3].pop(3)
print('Here is the Solution')
print(play[1])
print(play[2])
print(play[3])