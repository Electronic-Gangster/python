#리스트안에서 for문 활용하기

import turtle as t
list=["red", "blue", "green", "yellow", "purple", "black"]

t.speed(0)

#방법 1
# for count in range(6): #0~5까지 반복
#     t.begin_fill()
#     t.color(list[count])
#     t.circle(100)
#     t.left(360/6)
#     t.end_fill()

#방법 2
for idx in list:  #list에 있는 값만큼 반복
    t.begin_fill()
    t.color(idx)
    #print(list.index(item),item) #인덱스 값과 거기에 해당 하는 색상 출력
    t.circle(100)
    t.left(360/6)
    t.end_fill()

t.exitonclick()