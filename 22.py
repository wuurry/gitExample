from ipaddress import *
n = ip_network('123.222.111.192/255.255.255.248')
k = 0
for i in n:
    b = bin(int(n))[2:].zfill(32)
    if b[-8:].count('0') % 3 != 0:
        k +=1
print(k)