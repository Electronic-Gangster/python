#list 타입의 각종 함수 연습
list=["red", "orange", "yellow", "green", "blue"]
print(list)
print(list.pop())   #마지막으로 입력된 데이터 꺼내기 (ex. blue)

list2=list.copy()   #list를 복사해서 list2에 넣기 (pop으로 꺼낸 데이터를 제외하고 복사)
print(list2)

list2.sort()        #오름차순 정렬
print(list)         #넣은 순서대로 출력
print(list2)        #정렬된 순서대로 출력

list.reverse()      #내림차순 정렬
print(list)         #넣은 순서의 반대로 출력

list.insert(1, "gray")  #1번째 위치(2번)에 gray를 삽입
print(list)

list.remove("gray")     #gray를 삭제
print(list)