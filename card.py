class Card:
  """Composition from class "Desk"
  Has:
    _rank: an integer index 0-12, 
          representing the card ranks of [‘2’, ‘3’, ‘4’, ‘5’, ‘6’,
          ‘7’, ‘8’, ‘9’, ‘10’, ‘Jack’, ‘Queen’, ‘King’, ‘Ace’].
    _suit: an integer index 0-3, 
          representing the card suits of [‘Clubs’, ‘Diamonds’, 
          ‘Hearts’, ‘Spades’]
 Does: 
    Create attribute of the cards: ranks,suits
    Display the cards.
    Compare two cards.
"""

  def __init__(self, suit, rank):
    self._suit = suit
    self._rank = rank

  """ Use a decorator to make the property for the Card’s rank attribute. """
  @property
  def rank(self):
    return self._rank

  def __str__(self):
    """ Returns a string in the format ‘rank of suit’ (ex. ‘King of Clubs’). """

    ranks = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
        'Ace'
    ]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    str_rank = ranks[self._rank]
    str_suit = suits[self._suit]
    return f"{str_rank} of {str_suit}\n"

  def __lt__(self, other):
    """Compares the ranks of the self and other cards"""
    return self._rank < other._rank
