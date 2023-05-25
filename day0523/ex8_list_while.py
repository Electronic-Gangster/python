#리스트를 활용한 while문 공부
import turtle
colors = ["red", "purple", "blue", "green", "yellow", "orange", "white", "cyan"]

t=turtle.Turtle()                   #거북이 모양의 객체 생성
turtle.bgcolor("black")             #배경색을 검은색으로 설정
t.speed(0)                          #거북이 속도를 가장 빠르게 설정
t.width(3)                          #거북이 선의 굵기를 3으로 설정
length=10                           #거북이 선의 길이를 10으로 설정

#반복문 while (한 탭 들어가서 작성해야 함)
while length<500:                #length가 500보다 작을 때까지 반복
    t.forward(length)              #거북이가 length만큼 앞으로 이동
    t.pencolor(colors[length%7])   #거북이 선의 색을 colors의 0~7번째 색으로 설정
    t.right(144)                   #거북이가 오른쪽으로 144도 회전
    t.circle(40)
    t.dot(10)
    t.stamp()                     #거북이 모양을 도장처럼 찍음 
    length += 5                    #length에 5를 더함
t.exitonclick()                    #클릭하면 종료