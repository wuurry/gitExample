res = []
for i in range(0, 82000, -1):
    if i > 80000:
        res.append(100)
    if i <= 80000:
        res.append(res[i+1]*i)
    print(i)

    