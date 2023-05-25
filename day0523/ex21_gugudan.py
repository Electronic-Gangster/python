# 숫자를 입력하면 해당 구구단 출력
# 단, 2~9가 아니면 "다시 입력해주세요" 출력
# 0을 입력하면 종료하면서 "구구단을 종료합니다" 출력
# 출력시 format을 사용해서 출력

# while True:
#     num = int(input("숫자를 입력하세요 (2~9, 0은 종료): "))
#     if num == 0:
#         print("구구단을 종료합니다.")
#         break
#     elif num < 2 or num > 9:
#         print("다시 입력해주세요.")
#         continue
    
#     print("=== {}단 ===".format(num))
#     for i in range(1, 10):
#         print("{} x {} = {}".format(num, i, num * i))

while True:
    dan=int(input("단을 입력하세요"))
    if dan==0:
        break
    if not 2<=dan<=9:
        print("다시 입력해주세요")
        continue
    for n in range(1,10):
        print("{} x {} = {}".format(dan, n ,dan*n))
    print("="*20)
print("프로그램 끝!!")