import turtle

turtle.speed(1)
turtle.bgcolor('white')

def draw_circle(x, y, radius, angle):
    # 시작 위치 설정
    turtle.up()
    turtle.goto(x, y - radius)
    turtle.down()
    
    turtle.seth(angle)
    
    arg = 1 - radius

    # 타원 그리기
    while y + radius - turtle.ycor() >= 0.5:
        turtle.left(1)
        turtle.forward(1)
        if arg < 0:
            arg += 2 * turtle.ycor() + 3
        else:
            arg += 2 * (turtle.ycor() - radius) + 5
            turtle.right(1)
            radius -= 1

# 로고의 네 가지 원 그리기
turtle.fillcolor('black')
turtle.begin_fill()
draw_circle(-50, 0, 50, 0)
draw_circle(50, 0, 50, 180)
turtle.end_fill()

turtle.begin_fill()
draw_circle(-50, 0, 40, 0)
draw_circle(50, 0, 40, 180)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
