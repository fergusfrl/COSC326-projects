# Fergus Farrell
# Etude 4 - Peanuts and Pretzels

def printtable(table):
    for x in table:
        print x

def generatetable(size, moves):
    table = []
    for i in range(size):
        table.append(False)

    for i in range(len(moves)):
        for j in range(moves[i] - 1, size, moves[i] * 2):
            table[j] = True
    return table

moves = []
moves.append(1)
moves.append(2)
moves.append(3)  # legal moves
peanutSize = 12  # number of peanuts
pretzelSize = 12
peanutwinning = generatetable(peanutSize, moves)
pretzelwinning = generatetable(pretzelSize, moves)
print 'Peanut Table:'
printtable(peanutwinning)
print '\nPretzel Table:'
printtable(pretzelwinning)

if peanutwinning[len(peanutwinning)-1] or pretzelwinning[len(pretzelwinning)-1]:
    print '\n0 0'
else:
    print '\nIt is posible to win. How? Shhhhh.'
