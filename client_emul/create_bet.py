from random import randint
from currencies import currencies

def generate_numbers_for_bet():
    count = randint(6,15)
    bet = []
    while count != 0:
        bet.append(randint(1,36))
        count -= 1
    return bet

def generate_bet():
    bet = {
        "user_id": randint(100000,10000000),
        "edition": "Don't forget to make logic with DB",
        "game_id": randint(100000,10000000),
        "game_name": "Lucky Numbers",
        "bet_sum": randint(1,1000),
        "currency_id": 978,
        "currency_name": "Euro",
        "bet": generate_numbers_for_bet(),
    }
    return bet

if __name__ == "__main__":
    generate_bet()