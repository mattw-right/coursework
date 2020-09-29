
import matplotlib.pyplot as plt
import os
from scipy import spatial

tracks = os.listdir(path='./fouriers/')
fouriers = {}

for i in tracks:
    try:
        fouriers[i] = [float(i) for i in open('./fouriers/' + i).read().split('\n')[:-1]]
    except:
        pass

fouriers

list(fouriers.keys())[0]
fouriers['Walk On the Wild Side.txt']

likes = ['Like a Rolling Stone.txt', 'Visions of Johanna.txt']

D = {}
for k in likes:
    differences = {}
    for i in list(fouriers.keys()):
        differences[i] = spatial.distance.cosine(fouriers[k], fouriers[i])
    D[k] = differences





sD = {}

for i in list(D[likes[0]].keys()):
    sD[i[:2]] = D[likes[0]][i]


plt.bar(range(len(sD)), list(sD.values()), align='center')
plt.xticks(range(len(sD)), list(sD.keys()))
plt.show()


out = {}

for i in tracks:
    if i not in likes:
        out[i] = 0

for i in likes:
    for j in list(D[i].keys()):
        if j not in likes:
            out[j] += D[i][j]

{k: v for k, v in sorted(out.items(), key=lambda item: item[1])}
