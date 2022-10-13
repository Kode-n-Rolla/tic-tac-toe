import random
from board import Board
from cell import Cell
from player import Player


def game():
    this_deck = Board()
    my_cell = Cell()
    name = input('Your name is ')
    while True:
        choice_elem = input('\nWhat do you want to play?: ').upper()
        person = Player(name, choice_elem)

        if choice_elem == 'X':
            print(f'{person.name} move first.')
            break
        elif choice_elem == 'O':
            print('AI move first.')
            break
        else:
            print('Error input!')

    move_list = []
    ai_move_list = []
    this_deck.print_board()
    while True:

        try:
            my_cell.check_winner()
            if my_cell.check_winner() == True:
                print('Winner is X')
                break
            elif my_cell.check_winner() == False:
                print('Winner is 0')
                break
            if choice_elem == 'X' or choice_elem == 'Х':
                ai_elem = 'O'
                move = int(input('\nNumber of place move? '))
                if my_cell.add_and_check(move, choice_elem) == False:
                    move = int(input('\nNumber of place move? '))
                    move_list.append(move)
                    my_cell.add_and_check(move, choice_elem)
                move_list.append(move)
                this_deck.new_board(move, choice_elem)

                ai_move = random.choice([i for i in range(0, 9) if i not in move_list
                                         and i not in ai_move_list])
                ai_move_list.append(ai_move)
                print('AI move:', ai_move)
                this_deck.new_board(ai_move, ai_elem)

            elif choice_elem == 'O' or choice_elem == 'О':
                ai_elem = 'X'
                ai_move = random.choice([i for i in range(0, 9) if i not in move_list
                                         and i not in ai_move_list])
                ai_move_list.append(ai_move)
                print('AI move:', ai_move)
                this_deck.new_board(ai_move, ai_elem)
                move = int(input('\nNumber of place move? '))
                if my_cell.add_and_check(move, choice_elem) == False:
                    move = int(input('\nNumver of place move? '))
                    move_list.append(move)
                    my_cell.add_and_check(move, choice_elem)
                move_list.append(move)
                this_deck.new_board(move, choice_elem)

        except IndexError:
            print('Friendly is winner!')
            break


game()
