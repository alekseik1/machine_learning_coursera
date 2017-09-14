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
            all_words[word] = k
            k += 1


res = np.array([[0]*len(all_words) for i in np.arange(len(sentences))])
for i, s_words in enumerate(words):
    co = Counter(s_words)
    for j in co:
        res[i][all_words[j]] = co[j]

#print res[0][all_words['osx']]

distances = []
for i in range(1, len(res)):
    distances.append(spatial.distance.cosine(res[0], res[i]))
s_distances = sorted(distances)

print distances.index(s_distances[0])
print distances.index(s_distances[1])

# PROVE

#tmp = [no for no, x in enumerate(res[0]) if x != 0]
#print(tmp)
#for j in tmp:
#    print [i for i, x in all_words.iteritems() if x == j]