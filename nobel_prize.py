import requests

from constants import HELP_STRING

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

def main():
    print(HELP_STRING)
    while True:
        user_input = input(">")
        # exit program if q or Q is entered
        if user_input == "q" or user_input == "Q":
            break
        # print help if h or H is entered
        if user_input == "h" or user_input == "H":
            print(HELP_STRING)
            continue
        year, field = user_input.split()
        eng_field = field_dict[field]
        eng_field = {"nobelPrizeYear": int(year), "nobelPrizeCategory": eng_field}

        nobel_prizes = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=eng_field).json()
        # TODO 5p  Lägg till någon typ av avskiljare mellan pristagare, exempelvis --------------------------

        # TODO 20p Skriv ut hur mycket pengar varje pristagare fick, tänk på att en del priser delas mellan flera mottagare, skriv ut både i dåtidens pengar och dagens värde
        #   Skriv ut med tre decimalers precision. exempel 534515.123
        #   Skapa en funktion som hanterar uträkningen av prispengar och skapa minst ett enhetestest för den funktionen
        #   Tips, titta på variabeln andel
        # Feynman fick exempelvis 1/3 av priset i fysik 1965, vilket borde gett ungefär 282000/3 kronor i dåtidens penningvärde

        for prize in nobel_prizes["nobelPrizes"]:
            prize_money = prize["prizeAmount"]
            prize_money_current_value = prize["prizeAmountAdjusted"]
            print(f"{prize['categoryFullName']['se']}, prissumma {prize_money} SEK")

            for laureate in prize["laureates"]:
                print(laureate['knownName']['en'])
                print(laureate['motivation']['en'])
                andel = laureate['portion']
                print('-' * 20)



if __name__ == '__main__':
    main()
    