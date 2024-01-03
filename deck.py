from card import Card
import random


class Deck:
  """Composition with class "Card": 
    Desk has created several Room objects that are stored in the Desk list"""

  def __init__(self):
    """_cards: a list of Card objects that are in the deck
      – Initializes a standard deck of 52 cards. Thirteen ranks of each of 
      the four suits."""
    self._card = [Card(suit, rank) for suit in range(4) for rank in range(13)]

  def shuffle(self):
    """Initializes a standard deck of 52 cards. Thirteen ranks of each of 
      the four suits"""
    random.shuffle(self._card)

  def draw_card(self):
    """Remove the topmost card from the deck and return it"""
    return self._card.pop()

  def __len__(self):
    """– return the number of cards remaining in the deck."""
    return len(self._card)
