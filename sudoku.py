#게임 룰
#어느 곳에 넣을 지 선택
#숫자 넣기
#9칸 안에 숫자(1, 2, 3)가 들어가야한다.
#한줄에 서로 다른 숫자가 들어가야한다.
print('=======================')
print('        sudoku         ')
print('=======================')

board = [''
         , ' ', ' ', ' '
         , ' ', ' ', ' '
         , ' ', ' ', ' ']
game_length = 9

def show_board():
    print('\t\t' + board[1] + '|' + board[2] + '|' + board[3])
    print('\t\t' + '-+-+-')
    print('\t\t' + board[4] + '|' + board[5] + '|' + board[6])
    print('\t\t' + '-+-+-')
    print('\t\t' + board[7] + '|' + board[8] + '|' + board[9])

while True:
    show_board()
    # 리스트 위치 선택
    user_location = []
    user_location.append(input('location >'))

    #사용자 입력값을 위치에 넣음
    for i in range(game_length):
        for j in range(game_length):
            if user_location[i] == board[j]:
                if i == j:
                    user_input = int(input('num > ' + board[i]))
                    board[user_input].insert(user_location, user_input)
                    break
    #     if user_location[i] == board[i]:
    #                             user_input = int(input('num > ' + board[i]))
    #                             board[user_input].insert(user_location, user_input)
    #                         show_board()
    #
    # if 1 > user_input or user_input > 3:
    #     print('1 ~ 3사이에 숫자만 입력하세요. ')
    #     continue
    # if board[user_input] != ' ':
    #     print('이미 입력한 값입니다.')
    #     continue
    # if ((board[1] == board[2] == board[3])
    #         or (board[4] == board[5] == board[6])
    #         or (board[7] == board[8] == board[9])
    #         or (board[1] == board[4] == board[7])
    #         or (board[2] == board[5] == board[8])
    #         or (board[3] == board[6] == board[9])):
    #     print('다른 숫자를 넣어주세요. ')
    #     continue
    # break