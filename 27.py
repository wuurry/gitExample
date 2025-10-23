cluster1 = []
cluster2 = []
cluster3 = []
t = 0
for i in open('27B_22625.txt'):
    x,y = [float(x) for x in i.split()]
    if y > 20:
        cluster1.append([x,y])
    if 20 > y > 10:
        cluster2.append([x,y])
    if y < 10:
        cluster3.append([x,y])
    t += 1
print(len(cluster1), len(cluster2), len(cluster3),t)
def centroid(cluster):
    x_ancen = 0
    y_ancen = 0
    x_cen = 0
    y_cen = 0
    maxt = 0
    mint = 1111111110
    for i in range(len(cluster)):
        r = 0
        for j in range(len(cluster)):
            x1 = cluster[i][0]
            y1 = cluster[i][1]
            x2 = cluster[j][0]
            y2 = cluster[j][1]
            r += ((x2-x1)**2 + (y2-y1)**2)**0.5
        if r > maxt:
            maxt = t
            x_ancen = x1
            y_ancen = y1
        if r < mint:
            mint = t
            x_cen = x1
            y_cen = y1
    return x_cen, y_cen, x_ancen, y_ancen

x1,y1,xa1,ya1 = centroid(cluster1)
x2,y2,xa2,ya2 = centroid(cluster2)
x3,y3,xa3,ya3 = centroid(cluster3)
print(int(((x1+x2+x3)/3)*10000), int(((ya1+ya2+ya3)/3)*10000))