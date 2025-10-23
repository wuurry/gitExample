for a in range(1000):
    c = 0
    for x in range(100):
        for y in range(100):
            if (x**2 <= 136) or (y < (4*x + a-70)) or (2*y > 51):
                c += 1
    if c == 10000:
        print(a)
        break