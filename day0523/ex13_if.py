#if문 연습 심화

#if문 조건 : 점수를 입력 후 0~100이 아니면 다시 입력
#점수에 따른 평가 출력

while True:
    score=int(input("점수입력(종료:999)"))
    if score==999:
        break

    if score<0 and score>100:
        print("점수를 다시 입력하세요")
        continue
    print("점수는 {}점 입니다.".format(score))

    #if로 평가
    if score>=90:
        평가="A"
    elif score>=80:
        평가="B"
    else:
        평가="C"
    
    print("점수 {}점: {}".format(score, 평가))
    
print("프로그램 종료")