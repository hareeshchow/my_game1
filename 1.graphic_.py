

n=int(input('enter 1 or 2:'))
if n==1:

    from turtle import *
    from colorsys import *
    bgcolor('black')
    tracer(100)
    pensize(1)
    h = 0

    for i in range(300):
        c=hsv_to_rgb(h,1,1)
        h += 0.05
        color(c)
        fillcolor()
        begin_fill()
        up()
        fd(i*2)
        down()
        rt(90)
        for j in range(50):
            fd(i)
            rt(144)
        end_fill()
    done()
elif n==2:
    import turtle as t
    import colorsys
    t.bgcolor('black')
    t.tracer(100)
    t.pensize(10)
    h=0.1
    t.up()
    t.goto(10,100)
    t.down()
    for i in range(260):
        c=colorsys.hsv_to_rgb(h,1,1)
        h += 0.02
        t.color(c)
        t.up()
        t.fd(i*2)
        t.down()
        t.circle(i,-100)
        t.fd(i)
        t.circle(i,-100)
    t.down
elif n==3:
    from turtle import *
    import turtle as t
    import colorsys
    bgcolor('yellow')
    pensize(2)
    tracer(50)
    h = 0
    for i in range(750):
        c=colorsys.hsv_to_rgb(h,1,1)
        h+=0.005
        up()
        goto(-8,25)
        fd(i)
        rt(89)
        fillcolor(c)
        begin_fill()
        circle(15,320)
        end_fill()
        lt(179)
        fd(i*2)
        rt(6)
    done()
