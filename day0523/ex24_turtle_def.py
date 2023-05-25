import turtle as t
import random as r
#이동할 거리길이를 입력해서 반환하는 함수 (입력 다이얼로그로 받기)

def inp():
    n=int(t.textinput("입력","이동할 거리를 입력하세요"))
    return n

list=["red","green","blue","yellow","purple","orange","black","white","gray","brown"]
t.shape("turtle")
t.width(3) #거북이 선 두께
t.speed(0) #거북이 속도
t.shapesize(3) #거북이 크기

while True:
    n=inp()
    if n==0:
        print("프로그램을 종료합니다")
        break
    idx=r.randint(0,9) #0~9사이의 정수 난수 발생
    t.color(list[idx]) #거북이 색상
    t.fd(n) #거북이 이동
    t.setheading(abs(n)) #거북이 방향
t.exitonclick() #클릭시 종료