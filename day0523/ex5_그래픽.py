import turtle as t
wn=t.Screen()               # 그림이 그려질 화면을 생성
wn.setup(600, 600, 0, 0)    # 너비, 높이, x좌표, y좌표
t.width(10)                  # 선의 굵기를 10으로 설정
#wn.colormode(1.0)           # 컬러 모드를 1.0으로 설정
#t.color(0, 1.0, 0.3)        # 펜의 색상을 초록색으로 설정

t.shape("turtle")           # 커서의 모양을 거북이로 설정
wn.colormode(255)           # 컬러 모드를 255로 설정
t.color(255, 0, 255)          # 펜의 색상을 핑크색으로 설정
t.fd(100)                  # 앞으로 100픽셀 이동
t.lt(120)                  # 왼쪽으로 120도 회전
t.fd(100) 
t.lt(120)
t.fd(100)
t.circle(100)             # 반지름이 100인 원을 그림
t.exitonclick()             # 마우스 클릭 시 종료
