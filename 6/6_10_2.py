from turtle import * 

tracer(0)
scl = 20
x= 0
y = 0
up()
for i in range(10):
    goto(x+ 0*scl,y+ 2*scl)
    dot(5,"red")
    goto(x + 2*scl,y + 0*scl)
    dot(5,"red")
    goto(x+ 0*scl,y+ 10*scl)
    dot(5,"red")
    goto(x- 2*scl,y- 0*scl)
    dot(5,"red")
    goto(x+ 0*scl, y+ 2*scl)
    dot(5,"red")
    goto(x+ 6*scl,y+6*scl)
    dot(5,"red")

update()
done()