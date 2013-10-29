import pickle
game = [120, 'Magician', ['spells', 'invisibility']]
print(game)
with open('game.pickle', 'wb') as f:
  pickle.dump(game, f)