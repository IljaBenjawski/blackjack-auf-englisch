import random
import time

print("******Blackjack******")

cards = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 1,
}


def moneyFunction():
    money_question = input(
        "Your current balance is 100$\nIncrease your balance by clicking 'b' or stay with 100$ by clicking 's'\nYour choice: ")
    return money_question


# Karten des Spielers
def hand_out_cards_to_player():
    player_cards_value = 0
    player_cards = []

    # Spieler erhält seine erste Karte
    card_name = random.choice(list(cards.keys()))
    cards_value = cards[card_name]
    if card_name == "Ace" and player_cards_value + 10 <= 21:
        cards_value += 10
        print("Softhand")
    player_cards.append((card_name, cards_value))
    player_cards_value += cards_value
    print(f"\nYour first card:\nCard: {card_name}\nValue: {cards_value}")

    player_move = input("\nClick(h) to hit a card\nClick(s) to stand\nYour Entry: ")
    while player_move == "h":
        card_name = random.choice(list(cards.keys()))
        cards_value = cards[card_name]
        if card_name == "Ace" and player_cards_value + 10 <= 21:
            cards_value += 10
            print("Softhand")

        print(f"\nDrawn card: {card_name}\nCard value: {cards_value}")

        player_cards.append((card_name, cards_value))
        player_cards_value = sum(card[1] for card in player_cards)
        print(f"\nTotal: {player_cards_value}\n")

        if player_cards_value == 21:
            print("You have a blackjack")
            break
        elif player_cards_value > 21:
            print("You are over 21")
            break
        player_move = input("\nClick(h) to hit a card\nClick(s) to stand\nYour Entry: ")

    print(f"Total: {player_cards_value}")
    return player_cards_value


def hand_out_to_dealer():
    dealer_cards = []
    dealer_cards_value = 0

    # Dealer erhält seine erste Karte
    card_name = random.choice(list(cards.keys()))
    card_value = cards[card_name]
    if card_name == "Ace" and dealer_cards_value + 10 <= 21:
        card_value += 10
        print("Softhand")
    dealer_cards.append((card_name, card_value))
    dealer_cards_value += card_value
    print(f"\nDealers first card:\nCard: {card_name}\nValue: {card_value}")

    time.sleep(1.5)

    # Dealer erhält seine zweite Karte (verdeckt)
    card_name = random.choice(list(cards.keys()))
    card_value = cards[card_name]
    print(f"\nDealers second card (hidden):\nCard: [Hidden]\nValue: [Hidden]")
    dealer_cards.append((card_name, card_value))

    return dealer_cards_value, dealer_cards


def comparison(dealer_cards_value, player_cards_value, money, balance):
    
        if dealer_cards_value > player_cards_value and dealer_cards_value < 21:
            print("Dealer won")
            balance = balance - money
            print(f"Your new balance is: {balance}")
        elif dealer_cards_value == 21 and player_cards_value == 21:
            print("Blackjack draw")
            print(f"Your balance remains: {balance}")
        elif dealer_cards_value == 21:
            print("Dealer has a Blackjack")
            balance = balance - money
            print(f"Your new balance is: {balance}")
        elif player_cards_value == 21:
            print("You have a Blackjack")
            new_money = money + money * 2  # Der Gewinn ist das Doppelte des Einsatzes
            balance = balance + new_money
            print(f"Your new balance is: {balance}")
        elif dealer_cards_value == player_cards_value:
            print("Draw")
            print(f"Your balance remains: {balance}")
        elif dealer_cards_value < player_cards_value and player_cards_value < 21:
            print("You won")
            balance = balance + money
            print(f"Your new balance is: {balance}")
        elif dealer_cards_value > 21 and player_cards_value > 21:
            print("Draw, nobody won")
            print(f"Your balance remains: {balance}")
        elif dealer_cards_value > 21 and player_cards_value < 21:
            print("You won")
            balance = balance + money
            print(f"Your new balance is: {balance}")
        elif player_cards_value > 21 and dealer_cards_value < 21:
            print("Dealer won")
            balance = balance - money
            print(f"Your new balance is: {balance}")
        else:
            print("There is a mistake")

        return balance  # Die aktualisierte Balance wird zurückgegeben

# while True endlose Schleife, kann nur mmit break gestoppt werden
def entry():
    while True:
        money_question = moneyFunction()  # money_question wird gespeichert

        if money_question == "s":
            balance = 100
            break
        elif money_question == "b":
            balance_input = input("Type in your balance: ")
            try:
                balance = int(balance_input)
                print(f"You entered: {balance}")
                break
            except ValueError:
                print("It has to be a number")
        else:
            print(f"\nInvalid entry: {money_question} you can only type s or b")

    while True:
        try:
            money_input = int(input("How much do you want to bet: "))  # Eingabe des Wetteinsatzes als Ganzzahl
            if money_input <= balance:  # Überprüfung, ob der Einsatz kleiner oder gleich dem Kontostand ist
                break  # Beenden der Schleife, wenn der Einsatz gültig ist
            else:
                print("You don't have enough money.")
        except ValueError:
            print("It has to be a number.")

    money = money_input  # money auf den gültigen Wetteinsatz setzen
    print(f"Your bet: {money}")
    return money, balance



# main Funktion
money, balance = entry()
player_cards_value = hand_out_cards_to_player()
print("Dealers Turn")
time.sleep(1.5)
dealers_value, dealer_cards = hand_out_to_dealer()
print("\n")
balance = comparison(dealers_value, player_cards_value, money, balance)

# Ausgabe basierend auf dem Ergebnis
if balance > 100:
    print("Congratulations! You won!")
elif balance == 100:
    print("It's a draw.")
else:
    print("Sorry, you lost.")
