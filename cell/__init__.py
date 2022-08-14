class Cell:

    def __init__(self):
        self.cell = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}

    def add_and_check(self, numb_cell, element):
        another_elem = ''
        if element == 'X':
            another_elem == 'O'
        elif element == 'O':
            another_elem == 'X'
        if self.cell[numb_cell] == numb_cell:
            self.cell[numb_cell] = element
            #print(self.cell)
            return True
        elif self.cell[numb_cell] == another_elem:
            print('Ход в эту клетку уже был сделан ранее! Переходи')
            return False
        elif self.cell[numb_cell] == element:
            print('Ход в эту клетку уже был сделан ранее! Переходи')
            return False

    def check_winner(self):
        if ((self.cell[0] == 'X' and self.cell[0] == self.cell[1] and self.cell[1] == self.cell[2])
            or (self.cell[3] == 'X' and self.cell[3] == self.cell[4] and self.cell[4] == self.cell[5])
            or (self.cell[6] == 'X' and self.cell[6] == self.cell[7] and self.cell[7] == self.cell[8])
            or (self.cell[0] == 'X' and self.cell[0] == self.cell[3] and self.cell[3] == self.cell[6])
            or (self.cell[1] == 'X' and self.cell[1] == self.cell[4] and self.cell[4] == self.cell[7])
            or (self.cell[2] == 'X' and self.cell[2] == self.cell[5] and self.cell[5] == self.cell[8])
            or (self.cell[0] == 'X' and self.cell[0] == self.cell[4] and self.cell[4] == self.cell[8])
            or (self.cell[2] == 'X' and self.cell[2] == self.cell[4] and self.cell[4] == self.cell[6])):
            return True
        elif ((self.cell[0] == 'O' and self.cell[0] == self.cell[1] and self.cell[1] == self.cell[2])
            or (self.cell[3] == 'O' and self.cell[3] == self.cell[4] and self.cell[4] == self.cell[5])
            or (self.cell[6] == 'O' and self.cell[6] == self.cell[7] and self.cell[7] == self.cell[8])
            or (self.cell[0] == 'O' and self.cell[0] == self.cell[3] and self.cell[3] == self.cell[6])
            or (self.cell[1] == 'O' and self.cell[1] == self.cell[4] and self.cell[4] == self.cell[7])
            or (self.cell[2] == 'O' and self.cell[2] == self.cell[5] and self.cell[5] == self.cell[8])
            or (self.cell[0] == 'O' and self.cell[0] == self.cell[4] and self.cell[4] == self.cell[8])
            or (self.cell[2] == 'O' and self.cell[2] == self.cell[4] and self.cell[4] == self.cell[6])):
            return False