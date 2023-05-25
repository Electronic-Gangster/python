s1="you see mofxcer"
s2="nice to meet you bxtch"
print(s1.startswith("mofxcer"))  #true
print(s1.startswith("nice"))  #false

print(s2.endswith("bxtch"))    #true

s3=s1.replace(" ","*")  #공백을 *로 변경
print(s3)

print(s1.count("e"))   #s1에서 e의 갯수 구하기

print(s1.lower(),s1.upper()) #소문자로 변환, 대문자로 변환

print('/'.join(s1)) #모든 글자 사이에 / 넣기

print(s2.isalpha()) #모두 알파벳일 경우 true
print(s2.isdigit()) #모두 숫자일 경우 true