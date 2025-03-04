from turtle import * 

tracer(0)
scl = 20
x= 0
y = 0

up()
goto(x-1.5*scl, y+0)
down()
for i in range(12):
    goto(x +1.5*scl,y+15*scl)
    dot(5,"red")
    goto(x+ 8*scl,y+ 0*scl)
    dot(5,"red")
    goto(x + 1.5*scl,y- 15*scl)
    dot(5,"red")
    goto(x -11*scl,y+0)
    dot(5,"red")

update()
done()