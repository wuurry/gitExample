f = open('1006.txt')
n, m = map(int, f.readline().split())
red = []
green = []

for i in f:
    t = list(map(int, i.split()))
    if len(t) > 1:
        red.append([t[0], 0])
        green.append([t[1], 1])
    else:
        red.append([t[0], 0])
boxes = red+green
boxes.sort(reverse=True)
k = 0
e = 9999
ind = 1
for i in range(len(boxes)):
    if (boxes[i][1] != ind) and (e - boxes[i][0] > 4):
        ind = boxes[i][1]
        k += 1
        e = boxes[i][0]
        print(e, ind, k)
print(k,e)