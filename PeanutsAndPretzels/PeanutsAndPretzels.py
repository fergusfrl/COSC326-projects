# Fergus Farrell
# Etude 4 - Peanuts and Pretzels

#Prints W/L table - will be unessessary in final product
def printtable(table):
    for x in table:
        print x

def generatetable(size, moves):
    table = []
    for i in range(size):
        table.append('W')

    for i in range(len(moves)):
        for j in range(moves[i] - 1, size, moves[i] * 2):
            table[j] = 'L'
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

if peanutwinning[len(peanutwinning)-1] == 'L' or pretzelwinning[len(pretzelwinning)-1] == 'L':
    print '\n0 0'
else:
    print '\nIt is posible to win. How? Shhhhh.'
