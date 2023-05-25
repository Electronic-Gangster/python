#5월 23일 거북이 이동시키는 함수 만들기
#조건 : list에 10개정도의 색상을 넣어놓고,
#      방향키를 움직일 때 마다 랜덤 색상으로 거북이가 해당 방향으로 10씩 이동시킨다.
#      거북이 크기, 굵기등은 모두 마음대로 한다.
#      space bar를 누르면 원래 위치로 이동한다 (0,0)

import turtle as t
import random as rnd

list=["red","green","blue","yellow","purple","orange","black","white","gray","brown"]

t.shape("turtle")
t.width(3) #거북이 선 두께
t.speed(0) #거북이 속도
t.shapesize(3) #거북이 크기

ws=t.Screen() #화면 객체
ws.colormode(255)  #색상 모드

t.shape("turtle") #거북이 모양
t.turtlesize(3) #거북이 크기

idx=rnd.randint(0,9) #0~9사이의 정수 난수 발생
t.color(list[idx]) #거북이 색상

#====이벤트 영역====#

def move_up():          
    t.setheading(90) #(위)
    t.forward(10)    #거북이가 10만큼 이동
def move_down():
    t.setheading(270) #(아래)
    t.forward(10)
def move_left():
    t.setheading(180) #(왼쪽)
    t.forward(10)
def move_right():
    t.setheading(360) #오른쪽
    t.forward(10)

def move_sp():
    idx=rnd.randint(0,9) #0~9사이의 정수 난수 발생
    t.color(list[idx]) #거북이 색상
    t.goto(0,0)

#====버튼 영역====#
t.onkeypress(move_up, "Up")      #키보드의 방향키 Up (호출할 함수명, 키값(첫글자 반드시 대문자)
t.onkeypress(move_down, "Down")  #키보드의 방향키 Down
t.onkeypress(move_left, "Left")  #키보드의 방향키 Left
t.onkeypress(move_right, "Right")#키보드의 방향키 Right
t.onkeypress(move_sp, "space")   #키보드의 space bar 이거는 소문자 ㅎㅎ

t.listen()                      #이벤트 처리 시작(키를 받을 수 있도록 포커스를 그래픽창으로 주는것)
t.exitonclick() #클릭하면 종료
