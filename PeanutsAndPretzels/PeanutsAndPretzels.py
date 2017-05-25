# Fergus Farrell
# Etude 4 - Peanuts and Pretzels

moves = []
winningHash = {}
winningList = []
moves.append(1)
moves.append(3)
moves.append(4)  # legal moves
pileSize = 11  # number of peanuts

for i in range(1, pileSize + 1):
    for j in range(len(moves)):
        if i - moves[j] == 0:
            winningHash[i] = True
for i in range(1, pileSize + 1):
    if winningHash.has_key(i):
        winningList.append(True)
    else:
        winningList.append(False)

print winningList