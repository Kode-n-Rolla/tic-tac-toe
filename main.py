import random
from board import Board
from cell import Cell
from player import Player


def game():
    this_deck = Board()
    my_cell = Cell()
    name = input('Твое имя: ')
    while True:
        choice_elem = input('\nЧем будешь играть? (ввод на английской раскладке(Х или О)): ').upper()
        person = Player(name, choice_elem)

        if choice_elem == 'X':
            print(f'{person.name} ходит первым.')
            break
        elif choice_elem == 'O':
            print('ИИ ходит первым.')
            break
        else:
            print('Ошибка ввода!')

    move_list = []
    ai_move_list = []
    this_deck.print_board()
    while True:

        try:
            my_cell.check_winner()
            if my_cell.check_winner() == True:
                print('Победители крестики')
                break
            elif my_cell.check_winner() == False:
                print('Победители нолики')
                break
            if choice_elem == 'X' or choice_elem == 'Х':
                ai_elem = 'O'
                move = int(input('\nКуда сходить? '))
                if my_cell.add_and_check(move, choice_elem) == False:
                    move = int(input('\nКуда сходить!? '))
                    move_list.append(move)
                    my_cell.add_and_check(move, choice_elem)
                move_list.append(move)
                this_deck.new_board(move, choice_elem)

                ai_move = random.choice([i for i in range(0, 9) if i not in move_list
                                         and i not in ai_move_list])
                ai_move_list.append(ai_move)
                print('Ход ИИ:', ai_move)
                this_deck.new_board(ai_move, ai_elem)

            elif choice_elem == 'O' or choice_elem == 'О':
                ai_elem = 'X'
                ai_move = random.choice([i for i in range(0, 9) if i not in move_list
                                         and i not in ai_move_list])
                ai_move_list.append(ai_move)
                print('Ход ИИ:', ai_move)
                this_deck.new_board(ai_move, ai_elem)
                move = int(input('\nКуда сходить? '))
                if my_cell.add_and_check(move, choice_elem) == False:
                    move = int(input('\nКуда сходить!? '))
                    move_list.append(move)
                    my_cell.add_and_check(move, choice_elem)
                move_list.append(move)
                this_deck.new_board(move, choice_elem)

        except IndexError:
            print('Победила дружба')
            break


game()