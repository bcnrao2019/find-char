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

# this comment was added at github page
# address of this file is https://github.com/bcnrao2019/find-char/edit/main/main.py
# time stamp 2021-07-11 19:08
