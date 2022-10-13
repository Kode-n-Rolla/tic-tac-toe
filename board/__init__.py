class Board:

    def __init__(self):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    """
    Output initial board
    """
    def print_board(self) -> str:
        print('\n', self.board[0], '|', self.board[1], '|', self.board[2])
        print('-----------')
        print('', self.board[3], '|', self.board[4], '|', self.board[5])
        print('-----------')
        print('', self.board[6], '|', self.board[7], '|', self.board[8])

    """
    Output board with moves
    """
    def new_board(self, move, player) -> str:
        if player == 'X':
            self.board[move] = 'X'
            print('\n', self.board[0], '|', self.board[1], '|', self.board[2])
            print('-----------')
            print('', self.board[3], '|', self.board[4], '|', self.board[5])
            print('-----------')
            print('', self.board[6], '|', self.board[7], '|', self.board[8])
        elif player == 'O':
            self.board[move] = 'O'
            print('\n', self.board[0], '|', self.board[1], '|', self.board[2])
            print('-----------')
            print('', self.board[3], '|', self.board[4], '|', self.board[5])
            print('-----------')
            print('', self.board[6], '|', self.board[7], '|', self.board[8])
