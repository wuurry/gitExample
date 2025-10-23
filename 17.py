with open('17_22468.txt') as f:
    res = [int(x) for x in f]
    c = 0
    k = 1111110
    m = 0
    t = e = 0
    for i in range(len(res)):
        t += res[i]
    m = t/len(res)
    print(m)
    for i in range(len(res)-1):
        e += 1
        if abs(res[i]+res[i+1]) > m:
            c += 1
            k = min(k, (res[i]+res[i+1]))
    print(c,abs(k))