from RandomClass import LCG

game_state = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
computer1 = LCG(seed=abs(hash('computer1')))
computer2 = LCG(seed=abs(hash('computer2')))
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

c1 = ''
c2 = ''
result = True


def win_checker(win, state):
    return win[0] in state and win[1] in state and win[2] in state


if chance:  # computer will start
    print('computer 1 will start')

    for i in range(1, 10):
        if i % 2 == 1:
            c1_choice = int((computer1.generate_random())*(10-i))
            c1 = c1 + str(game_state[c1_choice])
            game_state.pop(c1_choice)
            if win_checker(win[0], c1) or win_checker(win[1], c1) or win_checker(win[2], c1) or win_checker(win[3], c1)\
                    or win_checker(win[4], c1) or win_checker(win[5], c1) or win_checker(win[6], c1) \
                    or win_checker(win[7], c1):
                print('computer 1 wins')
                result = not result
                break

        else:
            c2_choice = int((computer2.generate_random())*(10-i))
            c2 = c2 + str(game_state[c2_choice])
            game_state.pop(c2_choice)
            if win_checker(win[0], c2) or win_checker(win[1], c2) or win_checker(win[2], c2) or win_checker(win[3], c2)\
                    or win_checker(win[4], c2) or win_checker(win[5], c2) or win_checker(win[6], c2)\
                    or win_checker(win[7], c2):
                print('computer 2 wins')
                result = not result
                break


else:   # player will start
    print('computer 2 will start')

    for i in range(1, 10):
        if i % 2 == 0:
            c1_choice = int(computer1.generate_random()*(10-i))
            c1 = c1 + str(game_state[c1_choice])
            game_state.pop(c1_choice)
            if win_checker(win[0], c1) or win_checker(win[1], c1) or win_checker(win[2], c1) or win_checker(win[3], c1)\
                    or win_checker(win[4], c1) or win_checker(win[5], c1) or win_checker(win[6], c1)\
                    or win_checker(win[7], c1):
                print('computer 1 wins')
                result = not result
                break
        else:
            c2_choice = int(computer2.generate_random()*(10-i))
            c2 = c2 + str(game_state[c2_choice])
            game_state.pop(c2_choice)
            if win_checker(win[0], c2) or win_checker(win[1], c2) or win_checker(win[2], c2) or win_checker(win[3], c2)\
                    or win_checker(win[4], c2) or win_checker(win[5], c2) or win_checker(win[6], c2)\
                    or win_checker(win[7], c2):
                print('computer 2 wins')
                result = not result
                break

print(c1)
print(c2)
# print(set(['7','8','9']) in set(['7', '8', '9', '4', '1']))
if not result:
    pass
else:
    print('draw')
