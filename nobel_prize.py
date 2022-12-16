# Teddy Fredricson

import requests
from constants import HELP_STRING, API

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1

field_dict = {
    "fysik": "phy",
    "kemi": "che",
    "litteratur": "lit",
    "ekonomi": "eco",
    "fred": "pea",
    "medicin": "med"
}


# TODO 10p programmet skall ge en hjälpsam utskrift istället för en krasch om användaren skriver in fel input
# TODO 15p om användaren inte anger ett område som exempelvis fysik eller kemi så skall den parametern inte skickas med
#      till apiet och vi får då alla priser det året


def prize_share_calc(prize_money: int, share: str) -> float:
    """
    Calculates the share of the prize money for each laureate.

    :param prize_money: The amount of money the prize is worth
    :param share: The share of the prize money the laureate gets
    :return: The amount of money the laureate gets
    """
    if share == "1/3":
        return round(prize_money / 3, 3)
    elif share == "1/2":
        return round(prize_money / 2, 3)
    elif share == "2/3":
        return round(prize_money / 3 * 2, 3)
    elif share == "1":
        return round(prize_money, 3)


def print_prize_winner(nobel_prizes: dict):
    """
    Prints the prize winner(s) for the given year and field.
    :param nobel_prizes: The dictionary containing the prize winners
    :return: None
    """
    for prize in nobel_prizes["nobelPrizes"]:
        prize_money = prize["prizeAmount"]
        prize_money_current_value = prize["prizeAmountAdjusted"]
        print('=' * 50)
        print(f"{prize['categoryFullName']['se']}, prissumma {prize_money} SEK ({prize_money_current_value} "
              f"SEK i dagens värde)")

        for laureate in prize["laureates"]:
            print(laureate['knownName']['en'])
            print(laureate['motivation']['en'])
            share = laureate['portion']
            print(f"Andel: {prize_share_calc(prize_money, share)} SEK")
            print('-' * 20)


def main():
    """
    Main function of the program.
    :return: None
    """
    print(HELP_STRING)
    while True:
        user_input = input(">")
        # exit program if q or Q is entered
        if user_input == "q" or user_input == "Q":
            break
        # print help if h or H is entered
        if user_input == "h" or user_input == "H" or user_input == "":
            print(HELP_STRING)
            continue
        year, field = user_input.split()
        eng_field = field_dict[field.lower()]
        eng_field = {"nobelPrizeYear": int(year), "nobelPrizeCategory": eng_field}
        nobel_prizes = requests.get(API, params=eng_field).json()
        print_prize_winner(nobel_prizes)


if __name__ == '__main__':
    main()
    