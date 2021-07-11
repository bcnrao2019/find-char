# a=[3,4,2,5,7,8,1,6]
# b=6
# output = [(2,4),(1,5)]
a = [3,4,2,5,7,8,1,6]
b=6
c = []
#d=0
for d in range(len(a)-1):
    for e in range(d+1, len(a)-1):
        if (a[d] + a[e]) == 6:
            c.append([a[d], a[e]])

print('list c:', c)

