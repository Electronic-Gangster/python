#list 자료형
list1=["hello"]
print(list1)

#데이터 추가
list1.append("world")
list1.append("python")
print(list1)

#선언만 할 때
list2=[]
list2.append("red")
list2.append("orange")
list2.append("yellow")
list2.append("green")
list2.append("blue")
print(list2)

#일부만 데이터를 출력
print("list1의 첫번째 데이터:",list1[0])
print("list2의 1~3 데이터:",list2[1:4])
print("list2의 2부터 끝까지 데이터:", list2[2:])

#다차원 배열 (리스트 안에 또 리스트를 담을 수 있다.)
list3=["아벤떼", "소나타", ["그랜저", "제네시즈"]]
print(list3)
print(list3[1])     #소나타가 출력
print(list3[2][0])  #그랜저가 출력