#!/usr/bin/env python3

"""Planets.py: The track of six planets in the solar system.

__author__ = "Sunpengwei"
__pkuid__  = "1800011718"
__email__  = "1800011718@pku.edu.cn"
"""

import turtle
import math
import random


turtle.hideturtle()
turtle.dot(30, "yellow")  # Draw the sun.

mercury = turtle.Turtle()
mercury.hideturtle()
mercury.shape("circle")
mercury.color("blue")
mercury.shapesize(0.15)
mercury.up()
mercury.setx(35)

venus = turtle.Turtle()
venus.hideturtle()
venus.shape("circle")
venus.color("green")
venus.shapesize(0.428)
venus.up()
venus.setx(55)

earth = turtle.Turtle()
earth.hideturtle()
earth.shape("circle")
earth.color("red")
earth.shapesize(0.5)
earth.up()
earth.setx(70)

mars = turtle.Turtle()
mars.hideturtle()
mars.shape("circle")
mars.color("black")
mars.shapesize(0.3)
mars.up()
mars.setx(85)

jupiter = turtle.Turtle()
jupiter.hideturtle()
jupiter.shape("circle")
jupiter.color("orange")
jupiter.shapesize(1.2)
jupiter.up()
jupiter.setx(110)

saturn = turtle.Turtle()
saturn.hideturtle()
saturn.shape("circle")
saturn.color("purple")
saturn.shapesize(0.75)
saturn.up()
saturn.setx(160)

comet = turtle.Turtle()  # Draw a comet.
comet.hideturtle()
comet.shape("circle")
comet.color("pink")
comet.shapesize(0.2)
comet.up()
comet.goto(-400, 200)

moon = turtle.Turtle()  # Draw the moon.
moon.hideturtle()
moon.shape("circle")
moon.color("brown")
moon.shapesize(0.15)
moon.up()
moon.setx(75)

for i in range(50):  # Draw 50 asteroids.
    if i <= 11:
        i = turtle.Turtle()
        i.hideturtle()
        i.shape("circle")
        i.color("gray")
        i.shapesize(0.08)
        i.up()
        randomnumber = 2 * random.random()
        a = math.cos(randomnumber * math.pi)
        b = math.sin(randomnumber * math.pi)
        i.goto(138*a - 47, 75 * b)
        i.showturtle()

    elif 11 < i <= 24:
        i = turtle.Turtle()
        i.hideturtle()
        i.shape("circle")
        i.color("gray")
        i.shapesize(0.08)
        i.up()
        randomnumber = 2 * random.random()
        a = math.cos(randomnumber * math.pi)
        b = math.sin(randomnumber * math.pi)
        i.goto(157*a - 55, 80 * b)
        i.showturtle()

    elif 24 < i <= 37:
        i = turtle.Turtle()
        i.hideturtle()
        i.shape("circle")
        i.color("gray")
        i.shapesize(0.08)
        i.up()
        randomnumber = 2 * random.random()
        a = math.cos(randomnumber * math.pi)
        b = math.sin(randomnumber * math.pi)
        i.goto(169*a - 65, 85 * b)
        i.showturtle()

    elif 37 < i <= 50:
        i = turtle.Turtle()
        i.hideturtle()
        i.shape("circle")
        i.color("gray")
        i.shapesize(0.08)
        i.up()
        randomnumber = 2 * random.random()
        a = math.cos(randomnumber * math.pi)
        b = math.sin(randomnumber * math.pi)
        i.goto(180*a - 75, 89 * b)
        i.showturtle()


def track(m, n, o, p, q, r, s, t):
    """Draw the elliptical tracks of planets.
    Draw a linear track of a comet.
    Draw a round track of the moon.
    """

    for i in [m, n, o, p, q, r]:
        i.showturtle()
        i.down()
    
    t.showturtle()
    
    for i in range(0, 2000, 10):
        am = math.cos(i / 180 * math.pi)
        bm = math.sin(i / 180 * math.pi)
        an = math.cos(i / 180 * math.pi / 1.4)
        bn = math.sin(i / 180 * math.pi / 1.4)
        ao = math.cos(i / 180 * math.pi / 1.9)
        bo = math.sin(i / 180 * math.pi / 1.9)
        ap = math.cos(i / 180 * math.pi / 2.5)
        bp = math.sin(i / 180 * math.pi / 2.5)
        aq = math.cos(i / 180 * math.pi / 3.2)
        bq = math.sin(i / 180 * math.pi / 3.2)
        ar = math.cos(i / 180 * math.pi / 4)
        br = math.sin(i / 180 * math.pi / 4)
        at = math.cos(i / 180 * math.pi * 5)
        bt = math.sin(i / 180 * math.pi * 5)
        m.goto(45*am - 10, 37 * bm)  # Draw the elliptical tracks.
        n.goto(70*an - 15, 50 * bn)
        o.goto(95*ao - 25, 60 * bo)
        p.goto(125*ap - 40, 70 * bp)
        q.goto(190*aq - 80, 93 * bq)
        r.goto(270*ar - 110, 140 * br)
        t.goto(95*ao - 25 + 10*at, 60*bo + 10*bt)  # Draw the round track.

        if i <= 500:
            s.showturtle()
            s.down()
            s.goto(1.6*i - 400, 200 - i)  # Draw the linear track.


def main():
    track(mercury, venus, earth, mars, jupiter, saturn, comet, moon)


if __name__ == "__main__":
    main()
