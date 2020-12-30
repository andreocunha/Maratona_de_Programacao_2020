
class Jogador:
  def __init__(self):
    self.games = 0
    self.points = 0



sequencia = input()
quemsaca = 1

jogador1 = Jogador()
jogador2 = Jogador()

for comando in sequencia:
  #print(f"{jogador1.games} ({jogador1.points}) - {jogador2.games} ({jogador2.points})  -  {quemsaca}")
  if comando == "S":
    if ((jogador1.games >=2) or (jogador2.games >= 2)):
      continue
    if quemsaca == 1:
      jogador1.points = jogador1.points + 1
      quemsaca = 1
      if jogador1.points >= 5:
        if (jogador1.points - jogador2.points) >= 2 or jogador1.points >= 10: #jogador1 ganhou o game
          jogador1.points = 0
          jogador1.games = jogador1.games + 1
          jogador2.points = 0
    else:
      jogador2.points = jogador2.points + 1
      quemsaca = 2
      if jogador2.points >= 5:
        if (jogador2.points - jogador1.points) >= 2 or jogador2.points >= 10: #jogador2 ganhou o game
          jogador2.points = 0
          jogador2.games = jogador2.games + 1
          jogador1.points = 0
  if comando == "R":
    if ((jogador1.games >=2) or (jogador2.games >= 2)):
      continue
    if quemsaca == 2:
      jogador1.points = jogador1.points + 1
      quemsaca = 1
      if jogador1.points >= 5:
        if (jogador1.points - jogador2.points) >= 2 or jogador1.points >= 10: #jogador1 ganhou o game
          jogador1.points = 0
          jogador1.games = jogador1.games + 1
          jogador2.points = 0
    else:
      jogador2.points = jogador2.points + 1
      quemsaca = 2
      if jogador2.points >= 5:
        if (jogador2.points - jogador1.points) >= 2 or jogador2.points >= 10: #jogador2 ganhou o game
          jogador2.points = 0
          jogador2.games = jogador2.games + 1
          jogador1.points = 0
  if comando == "Q":
    if jogador1.games >=2:
      print(jogador1.games, "(winner) -", jogador2.games)
    elif jogador2.games >=2:
      print(jogador1.games, "-", jogador2.games, "(winner)")
    elif quemsaca == 1:
      print(f"{jogador1.games} ({jogador1.points}*) - {jogador2.games} ({jogador2.points})")
    elif quemsaca == 2:
      print(f"{jogador1.games} ({jogador1.points}) - {jogador2.games} ({jogador2.points}*)")
