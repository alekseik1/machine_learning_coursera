import re
import numpy as np
from scipy import spatial
from collections import Counter

f = open('sentences.txt', 'r')
sentences = [i.lower() for i in f.read().split('\n') if i != ""]
words = []
for i, sentence in enumerate(sentences):
    tmp = []
    for j in re.split('[^a-z]', sentence):
        if j != "":
            tmp.append(j)
    words.append(tmp)

all_words = dict()
k = 0
for s_words in words:
    for word in s_words:
        if word not in all_words:
            all_words[word] = 0
        all_words[word] += 1
res = np.array([[0]*len(all_words) for i in np.arange(len(sentences))])

for i, s_words in enumerate(words):
    co = Counter(s_words)
    for j, word in enumerate(all_words):
        res[i][j] = co[word]
distances = []
for i in range(1, len(res)):
    distances.append(spatial.distance.cosine(res[0], res[i]))
print distances.index(min(distances))
print distances
