import mydef
import turtle

ws=turtle.Screen() #화면 객체
ws.colormode(255)  #색상 모드

#turtle 객체 생성
#list를 사용하여 거북이 100마리 생성
tlist=[]
for i in range(1,101):
    t=turtle.Turtle()
    tlist.append(t)

for t in tlist:
    mydef.showturtle(t)

turtle.exitonclick() #클릭하면 종료