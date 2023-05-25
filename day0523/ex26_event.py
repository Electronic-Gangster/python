import turtle as t

def mywrite(msg): #글쓰기 함수
    t.write(msg, font=("Arial", 24, "italic"), align="center")

def key_up():           #키보드 이벤트 함수
    t.clear()           #화면 지우기
    mywrite("Up Key!!") #글쓰기 함수 호출
def key_down():
    t.clear() 
    mywrite("Down Key!!")
def key_left():
    t.clear() 
    mywrite("Left Key!!")
def key_right():
    t.clear() 
    mywrite("Right Key!!")

def key_sp():
    t.clear() 
    mywrite("Space Key!!")


#이벤트 발생
t.onkeypress(key_up, "Up")      #키보드의 방향키 Up (호출할 함수명, 키값(첫글자 반드시 대문자)
t.onkeypress(key_down, "Down")  #키보드의 방향키 Down
t.onkeypress(key_left, "Left")  #키보드의 방향키 Left
t.onkeypress(key_right, "Right")#키보드의 방향키 Right
t.onkeypress(key_sp, "space")   #키보드의 space bar 이거는 소문자 ㅎㅎ
t.listen()                      #이벤트 처리 시작(키를 받을 수 있도록 포커스를 그래픽창으로 주는것)

#클릭하면 종료
t.exitonclick()