class Player :
  def play(self):
     print("The player is playing Cricket.")


class Batsman :
  def play(self):
     print("The Batsman is Batting.")


class Bowler :
  def play(self):
    print("The Bowler is Bowling.")

player = Player()
batsman = Batsman()
bowler = Bowler()
player.play()
batsman.play()
bowler.play()
