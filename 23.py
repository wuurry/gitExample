def f(n,m):
    if n == m:
        return 1
    if n > m:
        return 0
    if n == 27:
        return 0
    return f(n+3,m)+f(n+5,m)+f(n**2,m)
print(f(3,16)*f(16,51))