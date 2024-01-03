from card import Card


class Player:
  """Aggregation with class "Desk" """

  def __init__(self, deck):
    """_deck – a reference to the deck of cards that both the player and the dealer use.
      _hand – a list of Cards that the player is currently holding.
      Deals two cards to the player’s hand from the deck, then sorts the hand."""
    self._deck = deck
    self._hand = []
    for _ in range(2):
      self._hand.append(deck.draw_card())
    self._hand.sort()

  def hit(self):
    """adds another card from the deck to the player’s hand and resorts them."""
    self._hand.append(self._deck.draw_card())
    self._hand.sort()

  def score(self):
    """Totals up the cards in the player’s hand and returns that score.
      Card ranks 2-10 are face value, Jack, Queen, and King are 10,
      Aces are scored at 11 if the total score of the other cards is less than 22,
      otherwise they count as 1.
      """
    """card_value: a list of values for the ranks of the cards """
    card_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    total_score = 0
    total_aces = 0
    for card in self._hand:
      total_score += card_value[card._rank]
      if (card._rank == 12):
        total_aces += 1
    while (total_score > 21 and total_aces > 0):
      total_score -= 10
      total_aces -= 1
    return total_score

  def __str__(self):
    """displays each of the cards in the player’s hand 
      and the score of that hand"""
    card = "".join(str(card) for card in self._hand)
    return (f"\n{card}Score = {self.score()}")
