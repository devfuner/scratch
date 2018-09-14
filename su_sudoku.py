import operator
import random
from random import randrange

#게임 룰
#어느 곳에 넣을 지 선택
#숫자 넣기
#9칸 안에 숫자(1, 2, 3)가 들어가야한다.
#한줄에 서로 다른 숫자가 들어가야한다.
from functools import reduce

print('=======================')
print('        sudoku         ')
print('=======================')

board = [''
         , ' ', ' ', ' '
         , ' ', ' ', ' '
         , ' ', ' ', ' ']
game_length = 2

def show_board():
    print('\t\t' + board[1] + '|' + board[2] + '|' + board[3])
    print('\t\t' + '-+-+-')
    print('\t\t' + board[4] + '|' + board[5] + '|' + board[6])
    print('\t\t' + '-+-+-')
    print('\t\t' + board[7] + '|' + board[8] + '|' + board[9])

#랜덤 숫자
num = str(random.randrange(1, 4))
rand_locate = randrange(1, 9)
while True:
    board[rand_locate] = num
    break

while True:

    show_board()
     # 리스트 위치 선택
    user_location = int(input('location > '))
    # 선택한 칸에 넣을 숫자 입력
    user_input = input('number > ')
    # 사용자가 선택한 칸에 숫자 입력
    board[user_location] = user_input

    score = 0
    end_game = True
    for score in user_input:
        if board[user_location] == ' ':
            board[user_location] = score
            continue
        # (1~3사이의 숫자 입력)
        if 1 > int(score) or int(score) > 3:
            board[user_location] = ' '
            print('1 ~ 3 사이의 숫자를 입력해주세요 ')
            continue
    #중복검사
    for i in range(1, len(board)):
        for j in range(1, len(board)):
            if board[i][j] == set:
                set[i][j]
                print('DONE')
                break