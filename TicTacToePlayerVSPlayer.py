from RandomClass import LCG

game_state = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# player1 = LCG(seed=abs(hash('player1')))
# player2 = LCG(seed=abs(hash('player2')))
chance = True

win = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['1', '4', '7'],
    ['2', '5', '8'],
    ['3', '6', '9'],
    ['1', '5', '9'],
    ['3', '5', '7']
]

seed_value = abs(hash('starter'))
starter = LCG(seed=seed_value)

if int((10*(starter.generate_random()))) % 2 == 0:
    chance = chance
else:
    chance = not chance

p1 = ''
p2 = ''
result = True


def win_checker(win, state):
    return win[0] in state and win[1] in state and win[2] in state


if chance:  # computer will start
    print('player 1 will start')

    for i in range(1, 10):
        if i % 2 == 1:
            print(p2)
            p1_choice = input(f'please input a number from {game_state}:')
            p1 = p1 + p1_choice
            game_state.remove(p1_choice)
            # print(c)
            if win_checker(win[0], p1) or win_checker(win[1], p1) or win_checker(win[2], p1) or win_checker(win[3], p1)\
                    or win_checker(win[4], p1) or win_checker(win[5], p1) or win_checker(win[6], p1) \
                    or win_checker(win[7], p1):
                print('player 1 wins')
                result = not result
                break

        else:
            print(p1)
            p2_choice = input(f'please input a number from {game_state}:')
            p2 = p2 + p2_choice
            game_state.remove(p2_choice)
            if win_checker(win[0], p2) or win_checker(win[1], p2) or win_checker(win[2], p2) or win_checker(win[3], p2)\
                    or win_checker(win[4], p2) or win_checker(win[5], p2) or win_checker(win[6], p2)\
                    or win_checker(win[7], p2):
                print('player 2 wins')
                result = not result
                break


else:   # player will start
    print('player 2 will start')

    for i in range(1, 10):
        if i % 2 == 0:
            print(p2)
            p1_choice = input(f'please input a number from {game_state}:')
            p1 = p1 + p1_choice
            game_state.remove(p1_choice)
            if win_checker(win[0], p1) or win_checker(win[1], p1) or win_checker(win[2], p1) or win_checker(win[3], p1)\
                    or win_checker(win[4], p1) or win_checker(win[5], p1) or win_checker(win[6], p1)\
                    or win_checker(win[7], p1):
                print('player 1 wins')
                result = not result
                break
        else:
            print(p1)
            p2_choice = input(f'please input a number from {game_state}: ')
            p2 = p2 + p2_choice
            game_state.remove(p2_choice)
            if win_checker(win[0], p2) or win_checker(win[1], p2) or win_checker(win[2], p2) or win_checker(win[3], p2)\
                    or win_checker(win[4], p2) or win_checker(win[5], p2) or win_checker(win[6], p2)\
                    or win_checker(win[7], p2):
                print('player 2 wins')
                result = not result
                break

print(p1)
print(p2)
# print(set(['7','8','9']) in set(['7', '8', '9', '4', '1']))
if not result:
    pass
else:
    print('draw')
