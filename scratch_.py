
import matplotlib.pyplot as plt

s1 = [float(i) for i in open('./fouriers/Stranger.txt').read().split('\n')[:-1]]
s2 = [float(i) for i in open('./fouriers/All Along the Watchtower.txt').read().split('\n')[:-1]]
s3 = [float(i) for i in open('./fouriers/Clair de Lune, L. 32.txt').read().split('\n')[:-1]]

s12 = 0
for i in range(len(s1)):
    s12+= s2[i]-s1[i]

s13 = 0
for i in range(len(s1)):
    s13+= s3[i]-s1[i]


print(s12, s13)

plt.plot(s1)
plt.plot(s2)
plt.plot(s3)
plt.show()
