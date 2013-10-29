import pickle
# game = [120, 'Magician', ['spells', 'invisibility']]
with open('game.pickle', 'rb') as f:
  game = pickle.load(f)
  
print(game)