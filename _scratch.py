
import matplotlib.pyplot as plt


#likes and dislikes to create a listener profile

LIKES = ['Like a Rolling Stone.txt', 'Visions of Johanna.txt']
DISLIKES = ['Clare de Lune (piano).txt', "Blowin' in the Wind.txt"]

likes = []
dislikes = []

for i in LIKES:
    try:
        likes.append([float(i) for i in open('./fouriers/' + i).read().split('\n')[:-1]])
    except:
        pass

for i in DISLIKES:
    try:
        dislikes.append([float(i) for i in open('./fouriers/' + i).read().split('\n')[:-1]])
    except:
        pass

profile = []

for i in range(len(likes[0])):
    profile.append((likes[0][i] + likes[1][i])/2)

for i in range(len(likes[0])):
    profile[i] -= (dislikes[0][i] + dislikes[1][i])/2

plt.plot(range(len(profile)), profile)
plt.savefig('likes dylan, dislikes classical.png')





DISLIKES = ['Perfect Day.txt', 'Walk On the Wild Side.txt']
LIKES = ['No Surprises.txt', "Born Confused.txt"]

likes = []
dislikes = []

for i in LIKES:
    try:
        likes.append([float(i) for i in open('./fouriers/' + i).read().split('\n')[:-1]])
    except:
        pass

for i in DISLIKES:
    try:
        dislikes.append([float(i) for i in open('./fouriers/' + i).read().split('\n')[:-1]])
    except:
        pass

profile = []

for i in range(len(likes[0])):
    profile.append((likes[0][i] + likes[1][i])/2)

for i in range(len(likes[0])):
    profile[i] -= (dislikes[0][i] + dislikes[1][i])/2

plt.plot(range(len(profile)), profile)
plt.savefig('likes classical, dislikes dylan.png')
