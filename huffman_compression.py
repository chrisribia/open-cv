import heapq
def makeTree(letterFrequencies):
    heap = []
    for lf in letterFrequencies:
        heapq.heappush(heap,[lf])

    while(len(heap) > 1):
        child0 = heapq.heappop(heap)
        child1 = heapq.heappop(heap)

        freq0,label0 = child0[0]
        freq1, label1 = child0[0]
        freq = freq0 + freq1
        label = ''.join(sorted(label0 + label1))
        node = [(freq, label) ,child0,child1]
        heapq.heappush(heap,node)
    return heap.pop()


def walkTree(codeTree,codeMap,codePrefix):
    if(len(codeTree) > 1):
        frequency,label = codeTree[0]
        codeMap[label] = codePrefix
    else:
        value,child0,child1 = codeTree
        walkTree(child0,codeMap,codePrefix+"0")
        walkTree(child1, codeMap, codePrefix + "1")
        return codeMap




def makeCodeMap(codeTree):
    codeMap = dict()
    walkTree(codeTree,codeMap,'')
    return codeMap


def encode(message,frequencies):
    codeMap = makeCodeMap(makeTree(frequencies))
    return ''.join([codeMap[letter] for letter in message])

def decode(encodedMessage, frequencies):
    codeTree=entireTree = makeTree(frequencies)
    decodedLetters = []
    for digit in encodedMessage:
        if (digit == '0'): codeTree[1]
        else : codeTree = codeTree[2]
        if(len(codeTree) == 1):
            frequncy,label = codeTree[0]
            decodedLetters.append(label)
            codeTree = entireTree

    return ''.join(decodedLetters)
def testEncode():
    print("testing encode ....",end='')
    frequencies = [(45,'a'),(13,'b'),(12,'c'),(16,'d'),(9,'e')
                   ,(5,'f')]
    message = 'abacdaebfa'
    encoded = encode(message,frequencies)
    assert (encoded =='010101001110110110111000')
    print("passed")

print(testEncode())
