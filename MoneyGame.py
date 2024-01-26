from RandomClass import LCG


def money_game(rounds):
    player_money = [25] * 20

    for i in range(rounds):
        # print(player_money,sum(player_money))
        for j in range(len(player_money)):
            if len(player_money) == 1:
                break
            seed_value = abs(hash(str(j+5454)))
            lcg_generator = LCG(seed=seed_value)
            payee = int(lcg_generator.generate_random()*(len(player_money)-1))
            # print(j)
            if payee < j:
                player_money[j] -= 1
                player_money[payee] += 1
            else:
                player_money[j] -= 1
                player_money[payee+1] += 1

        while 0 in player_money:
            player_money.remove(0)

    return player_money, sum(player_money)
