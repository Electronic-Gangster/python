# map은 키, 값 쌍으로 저장하는 데이터형태를 말한다.

# 1. 딕셔너리 생성
a={0:"zero", 1:"one", 2:"two", 3:"three", 4:"four"}
a2=a.copy()
print(a)
print(a2)

# 2. 딕셔너리에 값 추가
b=a.keys()
print(b)

# 3. key 값만 따로 얻기
c=a.values()
print(c)

# 4. key, value 쌍 얻기
print(a.get(0))
print(a.get(1))
print(a.get(2))
print(a.get(3))
print(a.get(4))

# 5. key로 value를 꺼내기
print(a.pop(0)) #0번지 값을 꺼낸 후 지움
print(a.pop(3)) #3번지 값을 꺼낸 후 지움
print(a)

# 6. key, value 쌍 얻기
print(a.items())