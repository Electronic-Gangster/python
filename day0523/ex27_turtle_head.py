import turtle as t

ws=t.Screen() #화면 객체
ws.colormode(255)  #색상 모드

t.shape("turtle") #거북이 모양
t.turtlesize(3) #거북이 크기
t.width(5) #거북이 선 두께

t.color(200, 100, 200) #거북이 색상

t.setheading(90) #거북이의 머리 방향을 90도로 설정 (위)
t.forward(100) #거북이가 100만큼 앞으로 이동

t.setheading(360) #거북이의 머리 방향을 90도로 설정 (오른쪽)
t.forward(100) #거북이가 100만큼 앞으로 이동

t.setheading(270) #거북이의 머리 방향을 90도로 설정 (아래))
t.forward(100) #거북이가 100만큼 앞으로 이동

t.setheading(180) #거북이의 머리 방향을 90도로 설정 (왼쪽)
t.forward(100) #거북이가 100만큼 앞으로 이동

t.exitonclick() #클릭하면 종료