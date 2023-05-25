import random as rnd
def mystar(num):
    for n in range(1,num+1):
        for i in range(1,n+1):
            print("🖕",end=" ")
        print()
    print("="*40)

#turtle 값을 인자로 받아서 색상과 크기를 랜덤하게 만드는 함수
def showturtle(tt):             #tt는 turtle 객체
    tt.penup()                  #펜을 올림
    tt.shape("turtle")          #거북이 모양
    r=rnd.randint(0,255)        #0~255사이의 정수 난수 발생
    g=rnd.randint(0,255) 
    b=rnd.randint(0,255)
    ts=rnd.randint(2,5)         #2~5사이의 정수 난수 발생

    tt.color(r,g,b)             #거북이 색상
    tt.turtlesize(ts)           #거북이 크기

    #위치도 랜덤
    x=rnd.randint(-300,300)
    y=rnd.randint(-300,300)
    tt.goto(x,y)
