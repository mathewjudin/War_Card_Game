# from suit import Suit
# from card import Card
from deck import Deck
from player import Player
from war_car_game import WarCardGame

player=Player("Mathew",Deck(is_empty=True))
computer=Player("Computer",Deck(is_empty=True),is_computer=True)
deck=Deck()

game= WarCardGame(player,computer,deck)

game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    answer= input("\n Are you ready for the next round?\n Press Enter to Continue. Enter X to Stop.")
    if answer.lower() == "x":
     break