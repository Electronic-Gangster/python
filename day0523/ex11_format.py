#format 함수 연습
a=6.56789
b=23
money=5678932
print(format(a,'8.3f')) #8자리를 확보하고 소수점 3자리까지 출력
print(format(b,'20d'))  #20자리를 확보하고 우측정렬
print(format(money,'3,d')) #3자리마다 ,를 찍어서 출력

#변환기호 : %f: 실수, %d: 정수, %s: 문자열, %c: 문자
num1=20
num2=45
print(num1,"+",num2,"=",num1+num2)
print("%d + %d = %d" %(num1,num2,num1+num2))

name="윤석열"
age=62
height=180.5
weight=78.9
print("이름:%s, 나이:%d, 키:%0.1f, 몸무게:%0.1f" %(name,age,height,weight))
print("내 이름은 {}이고 내 나이는 {}세입니다.".format(name,age))

