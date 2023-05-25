# C:\Users\bitcamp\AppData\Local\Programs\Python\Python311\Scripts
# cmd 에서 위경로로 이동
# pip3 install requests
# pip3 install vendor
import requests

# 네이버 카페 'zipsy'에 접속하기 위해 requests 모듈을 사용해요.
req = requests.get("https://cafe.naver.com/zipsy")

# 네이버 카페 'zipsy'의 웹 페이지 소스 코드를 가져와요.
html = req.text

# HTTP 헤더 정보를 가져와요.
header = req.headers

# HTTP 상태 코드를 가져와요. (200: 정상)
status = req.status_code

# HTTP 요청이 정상적으로 이루어졌는지 여부를 확인해요. (True/False)
is_ok = req.ok

print("**** html **")
# print(html)

print("** header **")
# print(header)

print("** status **")
print(status)

print("** is_ok **")
print(is_ok)


