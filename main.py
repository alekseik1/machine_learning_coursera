import re
import numpy as np
import scipy.spatial as sc

f = open('sentences.txt', 'r')
sentences = [i.lower() for i in f.read().split('\n') if i != ""]

words = [re.split('[^a-z]', i) for i in sentences]
res = []
for i in words:
    res.extend(i)
words = np.array(res)
words = np.delete(words, np.argwhere(words == ""))
d = dict()
k = 0
for i in words:
    if i not in d.values():
        d[k] = i
        k += 1

m = [[0]*k for i in range(len(sentences))]
for i in range(len(m)):
    for j in range(len(m[0])):
        k = 0
        words_tmp = re.split('[^a-z]', sentences[i])
        res1 = []
        for qwe in words_tmp:
            res1.extend(qwe)
        words_tmp = np.array(res1)
        words_tmp = np.delete(words_tmp, np.argwhere(words == ""))

        d1 = dict()
        k1 = 0
        for qwe in words_tmp:
            if qwe not in d1.values():
                d1[k1] = qwe
                k += 1
sc.distance.cosine()