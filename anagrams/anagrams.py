#Fergus Farrell, Emilio McFadzean
#Etude 7 - Finding Anagrams
import sys

def toBinary(string):
  binaryList = []
  for i in range(len(string)):
    if string[i] != ' ':
      binaryList.append('0')
    else:
      binaryList.append('1')
  binaryString = ''.join(str(x) for x in binaryList)
  return int(binaryString, 2)


def anagrams(lcount, remains, sofar=()):
    if not any(lcount):
        #if not duplicates...
        #if len(sofar) == len(set(sofar)):
        wordList.append(' '.join(sorted(sofar, key=len, reverse=True)))
    for j, word in enumerate(remains):
        ncount = tuple(x - y for x, y in zip(lcount, counts[word]))
        nwords = filter(lambda w: within(counts[w], ncount), remains[j:])
        anagrams(ncount, nwords, sofar + (word,))


words = []
for line in sys.stdin:
    words.append(line[:-1])

wordList = []
letters = 'abcdefghijklmnopqrstuvwxyz'
wordCount = lambda w: tuple(w.count(c) for c in letters)
counts = dict((word, wordCount(word)) for word in words)
within = lambda c1, c2: all(x <= y for x, y in zip(c1, c2))
word = sys.argv[1]
inputWord = wordCount(word)
maxNumWords = int(sys.argv[2])
words = filter(lambda w: within(counts[w], inputWord), words)
anagrams(inputWord, words)

binaryListList = {}
wordList.sort()
result = []

for i in range(len(wordList)):
    if binaryListList.has_key(toBinary(wordList[i])):
        binaryListList[toBinary(wordList[i])].append(wordList[i])
    else:
        binaryListList[toBinary(wordList[i])] = [wordList[i]]

for i in range(max(binaryListList) + 1):
    if binaryListList.has_key(i):
        for j in range(len(binaryListList[i])):
            if binaryListList[i][j] not in result:
                if binaryListList[i][j].count(' ') < maxNumWords:
                    print binaryListList[i][j]
                    result.append(binaryListList[i][j])