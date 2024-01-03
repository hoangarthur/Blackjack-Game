"""
  Description: A simplified version of the card game Blackjack.
  Two cards will be dealt to the player (the user) and to the dealer (the computer).
  Whoever has the highest score without going over 21 wins the round.
"""

import check_input
from deck import Deck
from player import Player
from dealer import Dealer


def display_winner(pScore, dScore, points):
  """ 
  Compares the points to see whether player or dealer busts (over 21 points).
  If player busts, dealer automatically wins, and vice versa.
  """
  print("")
  if pScore > 21 and dScore <= 21:
    print("Player busts!")
    print("Dealer wins.")
    points[1] += 1
  elif dScore > 21 and pScore <= 21:
    print("Dealer busts!")
    print("Player wins.")
    points[0] += 1
  elif dScore > 21 and pScore > 21:
    print("No one wins.")
  elif pScore > dScore:
    print("Player wins.")
    points[0] += 1
  elif pScore < dScore:
    print("Dealer wins.")
    points[1] += 1
  else:
    print("Tie")
  print(f"Player's points: {points[0]}\nDealer's points: {points[1]}")


def main():
  print("-Blackjack-")
  """
  Points stores the number of rounds the player and dealer have won.
  Index 0 is player's points and index 1 is dealer's points
  """
  points = [0, 0]
  playAgain = True
  """
  Loops to promp the player to hit or stay until the player does not want to play anymore.
  """
  while playAgain:
    deck = Deck()
    deck.shuffle()
    players = Player(deck)
    dealer = Dealer(deck)
    while True:
      print(f"\nPlayer's Cards: {players}")
      choice = check_input.get_int_range("1. Hit\n2. Stay\nEnter choice: ", 1,
                                         2)
      if choice == 1:
        players.hit()
        if players.score() > 21:
          print(f"\nPlayer's Cards: {players}")
          print("Bust!")
          #If the player busts, player cannot hit anymore, dealer's turn
          break

      else:
        #If the player chooses to stay, it will be dealer's turn
        break

    print(dealer.play())
    pScore = players.score()
    dScore = dealer.score()
    display_winner(pScore, dScore, points)
    playAgain = check_input.get_yes_no("Play again? (Y/N): ")


main()
