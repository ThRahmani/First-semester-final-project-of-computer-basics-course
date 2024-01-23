from RandomClass import LCG


def money_game(rounds):
    player_money = [25] * 20

    for i in range(rounds):

        seed_value = abs(hash(str(i+800)))
        lcg_generator = LCG(seed=seed_value)
        payer = int(lcg_generator.generate_random() * (21 - 1))

        seed_value = abs(hash(str(i + 1800)))
        lcg_generator = LCG(seed=seed_value)
        payee = int(lcg_generator.generate_random() * (21 - 1))
        player_money[payer] -= 1
        player_money[payee] += 1

    player_money = [money for money in player_money if money > 0]
    return player_money

# final_money_distribution = money_game(100000000000000)
# print("The final state of each player's money:", final_money_distribution)
