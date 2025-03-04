from turtle import * 

tracer(0)
scl = 20
x= 0
y = 0
for i in range(10):
    goto(x+ 6*scl,y+ 15*scl)
    dot(5,"red")
    goto(x- 5*scl,y- 5*scl)
    dot(5,"red")
    goto(x+ 2*scl,y+ 2*scl)
    dot(5,"red")
    goto(x- 1*scl,y- 10*scl)

