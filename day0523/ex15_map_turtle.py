#map 기능을 활용한 디자인 예제

import turtle as t
myshape={"반지름":"90", "색상":"red", "선두께":"10", "선색상":"blue"}

t.color(myshape.get("색상"))        #red
t.pencolor(myshape.get("선색상"))   #blue
t.width(myshape.get("선굵기"))      #10
t.begin_fill()
t.circle(int(myshape.get("반지름")))     #90
t.end_fill()
t.exitonclick()