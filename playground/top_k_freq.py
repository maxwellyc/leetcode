from collections import Counter
import heapq

class Element:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

def topKFrequent(k, keywords, reviews):
    '''
    k: int
    keywwords: list of string
    reviews: list of string
    '''
    word_list = []

    for review in reviews:
        word_list += set(review.lower().split())

    print (word_list)
    count = Counter(word_list)

    heap = []

    for word, freq in count.items():
        if word in keywords:
            heap.append([-freq,word])

    heap.sort()
    return [x[1] for x in heap][:k]

k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "cetracular is worse thsan anacell",
  "Betacellular is better than deltacellular.",
]
print(topKFrequent(k, keywords, reviews))
