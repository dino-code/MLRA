newList = []

g = open('fullList.csv', 'r')

oldList = g.read()
oldList = oldList.split(',')

for i in oldList:
    if i not in newList:
        newList.append(i)

print('newList length:', len(newList))
print('oldList length:', len(oldList))

f = open('newFullList.csv', 'w')
for i in newList:
    f.write(i+',')
g.close()