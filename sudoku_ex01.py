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

    # 입력할 칸의 번호를 입력한다.
    user_location = int(input('location >'))

    # 선택한 칸에 넣을 숫자를 입력한다.
    number = input('number >')

    # 사용자가 선택한 칸에 숫자를 입력한다.
    board[user_location] = number

    # 각각의 행과 열의 숫자가 하나씩만 있으면 게임에 성공했으므로 게임을 종료한다.
    # TODO 수림씨가 이 부분 만들어봐요~ ^^

    row_1 = len(set(board[1:4]))
    row_2 = len(set(board[4:7]))
    row_3 = len(set(board[7:]))
    col_1 = len(set([board[1], board[4], board[7]]))
    col_2 = len(set([board[2], board[5], board[8]]))
    col_3 = len(set([board[3], board[6], board[9]]))

    if 3 == row_1 == row_2 == row_3 == col_1 == col_2 == col_3:
        print("Success")
        break

