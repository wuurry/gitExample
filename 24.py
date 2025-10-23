with open('24_22446.txt') as f:
    s = f.readline()
    c = 0
    k = 0
    t = 0

    for i in range(len(s)):
        if s[i-2:i+1] == 'LND':
            c+=1
        while c > 10000:
            if s[t:t+3] == 'LND':
                c -= 1
            t += 1
        for x in range(t,i):
            if s[x]==s[i]:
                k = max(k, i-x+1)
                break
        if i % 100000 == 0:
            print(t,i)
print(k)