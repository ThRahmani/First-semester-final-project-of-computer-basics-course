from RandomClass import LCG

game_state = list({
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
})
print(game_state)
computer = LCG(seed=abs(hash('computer')))
player = LCG(seed=abs(hash('player')))
chance = True

win = [
    list('123'),
    list('456'),
    list('789'),
    list('147'),
    list('258'),
    list('369'),
    list('159'),
    list('357')
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

if chance:  # computer will start
    print('computer 1 will start')

    for i in range(1, 10):
        if i % 2 == 1:
            c1_choice = int((computer.generate_random())*(10-i) + 1)
            c1 = c1 + str(game_state[c1_choice])
            game_state.pop(c1_choice)
            if i == 5 and list(c1) in win:
                print('computer 1 wins')
                result = not result
                break
            elif i == 7 and (list(c1[:3]) in win or list(c1[1:]) in win):
                print('computer 1 wins')
                result = not result
                break
            elif i == 9 and (list(c1[:3]) in win or list(c1[1:4]) in win or list(c1[2:]) in win):
                print('computer 1 wins')
                result = not result
                break

        else:
            c2_choice = int((player.generate_random())*(10-i) + 1)
            c2 = c2 + str(game_state[c2_choice])
            game_state.pop(c2_choice)
            if i == 6 and list(c2) in win:
                print('computer 2 wins')
                result = not result
                break
            elif i == 6 and (list(c2[:3]) in win or list(c2[1:]) in win):
                print('computer 2 wins')
                result = not result
                break


else:   # player will start
    print('computer 2 will start')

    for i in range(1, 10):
        if i % 2 == 0:
            c1_choice = int(computer.generate_random()*(10-i) + 1)
            c1 = c1 + str(game_state[c1_choice])
            game_state.pop(c1_choice)
            if i == 6 and list(c1) in win:
                print('computer 1 wins')
                result = not result
                break
            elif i == 6 and (list(c1[:3]) in win or list(c1[1:]) in win):
                print('computer 1 wins')
                result = not result
                break
        else:
            c2_choice = int(player.generate_random()*(10-i) + 1)
            c2 = c2 + str(game_state[c2_choice])
            game_state.pop(c2_choice)
            if i == 5 and list(c2) in win:
                print('computer 2 wins')
                result = not result
                break
            elif i == 7 and (list(c2[:3]) in win or list(c2[1:]) in win):
                print('computer 2 wins')
                result = not result
                break
            elif i == 9 and (list(c2[:3]) in win or list(c2[1:4]) in win or list(c2[2:]) in win):
                print('computer 2 wins')
                result = not result
                break   

print(c1)
print(c2)

if not result:
    pass
else:
    print('draw')
