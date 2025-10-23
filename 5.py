for n in range(60):
    q = n
    b = ''
    res = []
    while n > 0:
        res.append(n % 7)
        b+= str(n % 7)
        n = n // 7
    s = b[::-1]
    if sum(res) % 2 == 0:
        s1 = s + '555'
    if sum(res) % 2 != 0:
        s1 = '33' + s + '6'
    r = int(s1, 7)
    print(q,b,res,s,sum(res),r)
