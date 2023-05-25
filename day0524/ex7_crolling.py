#pip3 install beautifulSoup4
import requests
from bs4 import BeautifulSoup

# 'https://music.bugs.co.kr/chart' 주소로 requests 모듈을 사용해서 웹 페이지에 접속해요.
req = requests.get('https://music.bugs.co.kr/chart')

# 웹 페이지의 HTML 소스 코드를 가져와서 'html' 변수에 저장해요.
html = req.text

# BeautifulSoup 객체를 생성하고, 가져온 HTML 소스 코드를 파싱해요.
soup = BeautifulSoup(html, 'html.parser')

# CSS 선택자를 사용해서 원하는 HTML 요소를 찾아요.
# 여기에서는 'p.title a'라는 CSS 선택자를 사용해요.
tiles = soup.select("p.title a")

# 찾아낸 HTML 요소들을 반복문을 통해 하나씩 가져와서 출력해요.
for atag in tiles:
    # 'tiles' 리스트에서 'atag' 요소의 인덱스와 텍스트를 출력해요.
    print(tiles.index(atag), ":", atag.text)


# 1. requests 모듈과 BeautifulSoup 모듈을 가져와요.
# 2. requests.get('https://music.bugs.co.kr/chart')를 사용해서 'https://music.bugs.co.kr/chart' 주소로 웹 페이지에 접속해요.
#  3.웹 페이지의 HTML 소스 코드를 가져와서 html 변수에 저장해요.
# 4. BeautifulSoup 객체를 생성하고, html 소스 코드를 파싱해서 객체로 변환해요.
# 5 .CSS 선택자를 사용해서 특정한 HTML 요소를 찾아요. 여기에서는 p.title a라는 CSS 선택자를 사용해서 원하는 요소를 찾아요.
# 6. 찾아낸 HTML 요소들을 반복문을 통해 하나씩 가져와서 출력해요. 이때, tiles.index(atag)는 tiles 리스트에서 atag 요소의 인덱스를 의미하고, atag.text는 atag 요소의 텍스트를 의미해요.
# 7. 프로그램을 실행하면, 음악 차트의 노래 제목들이 순서대로 출력되요. 예를 들어, "1: 노래1", "2: 노래2", "3: 노래3"과 같이 출력될 수 있어요.




