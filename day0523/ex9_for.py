#파이썬의 다양한 for문 문법

#1. for문의 기본 구조
for n in range(5):      #0부터 4까지 출력
    print(n,end=" ")    #end=" "는 줄바꿈을 하지 않고 한 줄에 출력하라는 의미
print()
print("="*30)           #=를 30번 반복해서 출력(구분선)

#2. for문의 기본 구조
for n in range(1,5):    #1~4까지 출력
    print(n,end=" ")    #end=" "는 줄바꿈을 하지 않고 한 줄에 출력하라는 의미
print()
print("="*30)           #(구분선)


#문제1. 1~100까지의 합을 구하기
sum = 0
for n in range(1,101):  #1~100까지 반복
    sum += n            #sum에 n을 더함
print("1~100까지의 합:",sum,"입니다.")