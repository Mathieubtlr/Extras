def tri(mots): # on fait un vieux tri à bulle
    n = len(mots)
    for i in range(n):
        for j in range(n):
            if mots[j] > mots[i]:
                mots[j] , mots[i] = mots[i] , mots[j]
    return mots


# parfois UTF-8 : open('text1.txt', 'r',encoding='utf-8')

file_read = open('text1.txt', 'r') 
lines = file_read.readlines()
mots = []

for line in lines:
    line = line.strip() 
    mots.append(line) 
file_read.close()

mots = tri(mots)

file_append = "text2" + ".txt"
file_append = open(file_append, "a")
for mot in mots:
    file_append.write(mot)
    file_append.write('\n')
file_append.close()