from turtle import *
k = 15
screensize(5000,5000)
tracer(0)
for i in range(4):
    fd(50*k)
    lt(90)
up()
fd(50*k)
lt(135)
pd()
for i in range(2):
    fd(102*k)
    lt(120)
    fd(182*k)
    lt(60)
up()
for x in range(-70,70):
    for y in range(-70,70):
        goto(x*k,y*k)
        dot(5)
done()