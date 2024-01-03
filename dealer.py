import player


class Dealer(player.Player):
  """Inheritance  from class "Player" """

  def play(self):
    """plays a round for the dealer. 
      The dealer hits on scores 16 or lower, 
      and stays on scores 17 or more"""
    while (self.score() <= 16):
      print(f"\nDealer's Cards:{str(self)}")
      print("Dealer Hits!")
      self.hit()

    return (f"\nDealer's Cards:{str(self)}")
