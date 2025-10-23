z = 0
for n in range(4000000, 66000000):
    b = ''
    q = n
    while n > 0:
        if n % 13 == 10:
            b += 'A'
        if n % 13 == 11:
            b += 'B'
        if n % 13 == 12:
            b += 'C'
        if n % 13 < 10:
            b += str(n % 13)
        n = n // 13
    s = b[::-1]
    if len(s) == 7:
        if s[0] != '0':
            if ('B1' not in s) and ('B3' not in s) and ('B5' not in s) and ('B7' not in s) and ('B9' not in s):
                if s.count('0') <= 1 and s.count('1') <= 1 and s.count('2') <= 1 and s.count('3') <= 1 and s.count('4') <= 1 and s.count('5') <= 1 and s.count('6') <= 1:
                    if s.count('7') <= 1 and s.count('8') <= 1 and s.count('9') <= 1 and s.count('A') <= 1 and s.count('B') <= 1 and s.count('C') <= 1:
                        if ('1B' not in s) and ('3B' not in s) and ('5B' not in s) and ('7B' not in s) and ('9B' not in s):
                            z +=1
                            if q % 1000000 == 0:
                                print(q,s,z)
print(z)
print(0)