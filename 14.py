a = 15*343**2031 + 7*49**1142 - 3*7**111 + 7**222 - 16809
b = ''
while a > 0:
    b += str(a % 7)
    a = a // 7
q = b.count('0') + b.count('2') + b.count('4') + b.count('6')
w = b.count('1') + b.count('3') + b.count('5')
print(q,w,q-w)