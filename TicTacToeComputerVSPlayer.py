from RandomClass import LCG

game_state = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
computer = LCG(seed=abs(hash('computer')))
player = LCG(seed=abs(hash('player')))
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

c = ''
p = ''
result = True


def win_checker(win, state):
    return win[0] in state and win[1] in state and win[2] in state


if chance:  # computer will start
    print('computer will start')

    for i in range(1, 10):
        if i % 2 == 1:
            c_choice = int((computer.generate_random())*(10-i))
            c = c + str(game_state[c_choice])
            game_state.pop(c_choice)
            # print(c)
            if win_checker(win[0], c) or win_checker(win[1], c) or win_checker(win[2], c) or win_checker(win[3], c)\
                    or win_checker(win[4], c) or win_checker(win[5], c) or win_checker(win[6], c) \
                    or win_checker(win[7], c):
                print('computer wins')
                result = not result
                break

        else:
            print(c)
            p_choice = input(f'please input a number from {game_state}:')
            p = p + p_choice
            game_state.remove(p_choice)
            if win_checker(win[0], p) or win_checker(win[1], p) or win_checker(win[2], p) or win_checker(win[3], p)\
                    or win_checker(win[4], p) or win_checker(win[5], p) or win_checker(win[6], p)\
                    or win_checker(win[7], p):
                print('player wins')
                result = not result
                break


else:   # player will start
    print('player will start')

    for i in range(1, 10):
        if i % 2 == 0:
            c_choice = int(computer.generate_random()*(10-i))
            c = c + str(game_state[c_choice])
            game_state.pop(c_choice)
            if win_checker(win[0], c) or win_checker(win[1], c) or win_checker(win[2], c) or win_checker(win[3], c)\
                    or win_checker(win[4], c) or win_checker(win[5], c) or win_checker(win[6], c)\
                    or win_checker(win[7], c):
                print('computer wins')
                result = not result
                break
        else:
            print(c)
            p_choice = input(f'please input a number from {game_state}: ')
            p = p + (p_choice)
            game_state.remove(p_choice)
            if win_checker(win[0], p) or win_checker(win[1], p) or win_checker(win[2], p) or win_checker(win[3], p)\
                    or win_checker(win[4], p) or win_checker(win[5], p) or win_checker(win[6], p)\
                    or win_checker(win[7], p):
                print('player wins')
                result = not result
                break

print(c)
print(p)
# print(set(['7','8','9']) in set(['7', '8', '9', '4', '1']))
if not result:
    pass
else:
    print('draw')