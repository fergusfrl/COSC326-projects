# Fergus Farrell
# Etude 4 - Peanuts and Pretzels

moves = []
winningHash = {}
winningList = []
moves.append(1)
moves.append(2)
moves.append(3)  # legal moves
pileSize = 12  # number of peanuts

for i in range(pileSize):
    winningList.append(False)
    
for i in range(len(moves)):
    for j in range(moves[i]-1, pileSize, moves[i]*2):
        winningList[j] = True

for x in winningList:
    print x
