#랜덤함수 예제
import random as r                      #random 모듈을 r이라는 이름으로 사용
import turtle as t                      #turtle 모듈을 t라는 이름으로 사용

# rnd=r.randint(1,100) #1~100까지의 랜덤한 숫자
# print(rnd)
ws=t.Screen()                           #스크린 객체 생성
ws.bgcolor("black")                     #배경색을 검정색으로 설정
ws.colormode(255)                       #색상 모드를 255로 설정

while True:
    x=int(input("x좌표 입력(종료:999)"))
    if x==999:
        print("종료")
        break
    
    y=int(input("y좌표 입력(종료:999)"))

    t.penup()                           #펜을 들어서 이동
    t.shape("turtle")                   #거북이 모양으로 설정
    t.goto(x,y)                         #x,y 좌표로 이동

    red=r.randint(0,255)                #0~255까지의 랜덤한 숫자
    green=r.randint(0,255)              #0~255까지의 랜덤한 숫자
    blue=r.randint(0,255)               #0~255까지의 랜덤한 숫자

    t.color(red,green,blue)             #색상을 랜덤으로 설정

    t.write("Good!!!", align="center", font=("Arial", 50, "normal")) #글자 출력