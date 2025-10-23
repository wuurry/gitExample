from fnmatch import *
for i in range(84318, 10**12, 84318):
    s = str(i)
    if s.count('0') <= 1 and s.count('1') <= 1 and s.count('2') <= 1 and s.count('3') <= 1 and s.count('4') <= 1 and s.count('5') <= 1:
        if s.count('6') <= 1 and s.count('7') <= 1 and s.count('8') <= 1 and s.count('9') <= 1:
            if fnmatch(str(i), '5*7?'):
                print(i, i//84318)







'''
def f(n):
    d = set()
    for i in range(1, int(n**0.5)+1):
        z = 0
        x = 0
        if n % i == 0:
            for j in range(1, int(i**0.5)+1):
                x = 0
                if i % j != 0:
                    z += 1
                if z == x:
                    d.add(i)
                    d.add(n // i)
                else:
                    break
    return sorted(d)
print(f(52))
'''