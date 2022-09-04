import random
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

from art import logo

def play_game():
    print(logo)
    #11 is the Ace.
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)
    
    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw!"
        elif computer_score == 0:
            return "You lose, dealer has Blackjack"
        elif user_score == 0:
            return "You win! You have a Blackjack"
        elif user_score > 21:
            return "Bust! You lose!"
        elif computer_score > 21:
            return "You win! The dealer went over!"
        elif user_score > computer_score:
            return "You win!"
        else:
            return "You lose!"
    
    user_cards = []
    computer_cards = []
    
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(cards):
        total = sum(cards)
        if total == 21 and len(cards) == 2:
            return 0
        if total > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
            total = sum(cards)
        return total

    user_still_drawing = True
    while user_still_drawing:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")
    
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        user_still_drawing = not is_game_over
        if not is_game_over:
            draw_card = input("Would you like to draw another card? 'y' or 'n'")
            if draw_card == "y":
                user_cards.append(deal_card())
            else:
                user_still_drawing = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    
while input("Do you want to play a game of Blackjack? 'y' or 'n': ") == "y":
    clear()
    play_game()
