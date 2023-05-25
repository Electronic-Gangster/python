#디자인으로 for문법 연습하기
import turtle as t  #turtle을 t로 설정

t.color("red")      #거북이 색을 빨간색으로 설정
t.begin_fill()      #색칠할 영역 시작
t.pencolor("blue")  #거북이 선의 색을 파란색으로 설정
t.width(5)          #거북이 선의 굵기를 5로 설정
t.shape("circle")   #거북이 모양을 원으로 설정 (circle, classic, triangle, turtle)

n=4 #n을 4로 설정
for x in range(n):  #n번 반복
    t.fd(100)       #거북이가 100만큼 앞으로 이동
    t.lt(360/n)     #거북이가 360/n만큼 왼쪽으로 회전
t.end_fill()        #색칠할 영역 끝
t.exitonclick()     #클릭하면 종료