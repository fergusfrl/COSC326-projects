#Fergus Farrell, Emilio McFadzean
#Etude 7 - Finding Anagrams
import sys


def binarySort(wList):
    global binaryList
    global maximum
    global binaryListList
    for i in range(len(wList)):
        for j in range(len(wList[i])):
            if wList[i][j] != ' ':
                binaryList.append('0')
            else:
                binaryList.append('1')
        binary = ''.join(binaryList)
        binary = int(binary, 2)
        if binary > maximum:
            maximum = binary
        if binaryListList.has_key(binary):
            binaryListList[binary].append(wList[i])
        else:
            binaryListList[binary] = [wList[i]]
        binaryList = []

    for i in range(maximum + 1):
        if binaryListList.has_key(i):
            for j in binaryListList[i]:
                print j
    binaryListList = {}


def anagrams(lcount, remains, sofar=()):
    if not any(lcount):
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
word = sys.argv[1].lower()
inputWord = wordCount(word)
maxNumWords = int(sys.argv[2])
words = filter(lambda w: within(counts[w], inputWord), words)
anagrams(inputWord, words)

binaryList = []
binaryListList = {}
wordList.sort()
result = []
lengthList = {}
maximum = 0

wordList.sort()
for i in range(len(wordList)):
  if lengthList.has_key(wordList[i].count(' ')):
    lengthList[wordList[i].count(' ')].append(wordList[i])
  else:
    lengthList[wordList[i].count(' ')] = [wordList[i]]
for i in range(max(lengthList)+1):
  if lengthList.has_key(i):
    binarySort(lengthList[i])
