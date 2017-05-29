#Fergus Farrell, Emilio McFadzean
#Etude 7 - Finding Anagrams
import sys

def sortString(string):
    array = string.split(' ')
    array.sort()
    array.sort(key=len, reverse=True)
    return ' '.join(array)

def toBinary(word):
    binaryString = ''
    for i in range(len(word)):
        if word[i] != ' ':
            binaryString = binaryString + '0'
        else:
            binaryString = binaryString + '1'
    return int(binaryString, 2)

def binarySort(wList):
    resultDir = {}
    for i in range(len(wList)):
        if resultDir.has_key(toBinary(wList[i])):
            if wList[i] not in resultDir[toBinary(wList[i])]:
                resultDir[toBinary(wList[i])].append(wList[i])
        else:
            resultDir[toBinary(wList[i])] = [wList[i]]
    for i in range(max(resultDir) + 1):
        if resultDir.has_key(i):
            for j in range(len(resultDir[i])):
                print resultDir[i][j]

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
wordList.sort()

for i in range(len(wordList)):
    wordList[i] = sortString(wordList[i])

lengthDir = {}
for i in range(len(wordList)):
    if lengthDir.has_key(wordList[i].count(' ')):
        lengthDir[wordList[i].count(' ')].append(wordList[i])
    else:
        lengthDir[wordList[i].count(' ')] = [wordList[i]]

for i in range(maxNumWords):
    if lengthDir.has_key(i):
        binarySort(lengthDir[i])