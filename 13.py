from ipaddress import *
n = ip_network('98.71.254.171/255.248.0.0', 0)
k = 0
for i in n:
    if str(bin(int(i))[2:]).count('1') % 7 == 0:
        print(i)
        break