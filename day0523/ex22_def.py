# 파이썬에서 함수 (모듈, 메서드) 선언하는 방법
# def 함수명 ([인수]):
#     코드1
#     코드2
#     [return 값]

#1. 함수선언
def func1():
    print("함수 호출!")

#2. 함수 호출
#func1() 함수 호출 방법
func1()
func1()


#3. 숫자를 인자로 받아서 1부터 해당 숫자까지 출력하는 함수
def numout(n):
    for i in range(1,n+1):
        print(i,end=" ")
    print()                     #줄넘김 대신 사용함

#위 함수 호출
numout(10)


#5. 숫자를 인자로 받아서 1부터 해당 숫자까지의 합을 출력하는 함수
def numsum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

#위 함수 호출
n1=numsum(10)
print(n1)

n2=numsum(365)
print(n2)

