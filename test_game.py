from game_logic import Board

def test_initial_board():
    board = Board()
    expected = [['','','',''],['','','',''],['','','',''],['','','','']]
    assert board.get_board() == expected
    assert board.get_current_player() == 'X'

def test_make_move_valid():
    board = Board()
    assert board.make_move(0, 0) == True
    assert board.get_board()[0][0] == 'X'
    assert board.get_current_player() == 'O'

def test_make_move_invalid():
    board = Board()
    board.make_move(0, 0)
    assert board.make_move(0, 0) == False
    assert board.get_current_player() == 'O'

def test_win_horizontal():
    board = Board()
    for col in range(4):
        board.make_move(0, col)
        if col < 3:
            board.make_move(1, col)
    assert board.check_win() == 'X'

def test_win_vertical():
    board = Board()
    for row in range(4):
        board.make_move(row, 0)
        if row < 3:
            board.make_move(row, 1)
    assert board.check_win() == 'X'

def test_win_diagonal():
    board = Board()
    for i in range(4):
        board.make_move(i, i)
        if i < 3:
            board.make_move(i, i+1)
    assert board.check_win() == 'X'

def test_win_diagonal_reverse():
    board = Board()
    for i in range(4):
        board.make_move(i, 3-i)
        if i < 3:
            board.make_move(i, 2-i)
    assert board.check_win() == 'X'

def test_draw():
    board = Board()
    # Set a draw board manually
    board.board = [
        ['X', 'O', 'X', 'O'],
        ['O', 'X', 'O', 'X'],
        ['X', 'X', 'X', 'O'],
        ['O', 'X', 'O', 'O']
    ]
    assert board.check_win() is None
    assert board.check_draw() == True

def test_reset():
    board = Board()
    board.make_move(0, 0)
    board.reset()
    expected = [['','','',''],['','','',''],['','','',''],['','','','']]
    assert board.get_board() == expected
    assert board.get_current_player() == 'X'

if __name__ == "__main__":
    test_initial_board()
    test_make_move_valid()
    test_make_move_invalid()
    test_win_horizontal()
    test_win_vertical()
    test_win_diagonal()
    test_win_diagonal_reverse()
    test_draw()
    test_reset()
    print("All tests passed!")