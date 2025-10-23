a = '0123456789ABC'
x = 0
z = 0
for q in a:
    for w in a:
        for e in a:
            for r in a:
                for t in a:
                    for y in a:
                        for u in a:
                            s = q+w+e+r+t+y+u
                            x += 1
                            if s[0] != '0':
                                if s.count('0') <= 1 and s.count('1') <= 1 and s.count('2') <= 1 and s.count('3') <= 1 and s.count('4') <= 1 and s.count('5') <= 1 and s.count('6') <= 1:
                                    if s.count('7') <= 1 and s.count('8') <= 1 and s.count('9') <= 1 and s.count('A') <= 1 and s.count('B') <= 1 and s.count('C') <= 1:
                                        if ('1B' not in s) and ('3B' not in s) and ('5B' not in s) and ('7B' not in s) and ('9B' not in s):
                                            z += 1
                                            print(x,s,z)
print(z)