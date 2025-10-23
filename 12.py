for n in range(4,1000):
    a = '>' + '0'*25 + n*'1' + '2'*25
    while '>1' in a or '>2' in a or '>0' in a:
        if '>1' in a:
            a = a.replace('>1', '22>', 1)
        if '>2' in a:
            a = a.replace('>2', '2>', 1)
        if '>0' in a:
            a = a.replace('>0', '1>', 1)
    s = a.count('2')*2 + a.count('1')*1
    if len(str(s)) == 4:
        if s % 15 == 0:
            print(n)
            break
print('-')