#pip3 install beautifulSoup4
import requests
from bs4 import BeautifulSoup

# 'https://music.bugs.co.kr/newest' 주소로 requests 모듈을 사용해서 웹 페이지에 접속해요.
req = requests.get('https://music.bugs.co.kr/newest')

# 웹 페이지의 HTML 소스 코드를 가져와서 'html' 변수에 저장해요.
html = req.text

# BeautifulSoup 객체를 생성하고, 가져온 HTML 소스 코드를 파싱해요.
soup = BeautifulSoup(html, 'html.parser')

# CSS 선택자를 사용해서 원하는 HTML 요소를 찾아요.
# 여기에서는 'section.sectionPadding div.albumTitle>a'라는 CSS 선택자를 사용해요.
tiles = soup.select("section.sectionPadding div.albumTitle>a")

# 찾아낸 HTML 요소들을 반복문을 통해 하나씩 가져와서 출력해요.
for atag in tiles:
    # 'tiles' 리스트에서 'atag' 요소의 인덱스와 텍스트를 출력해요.
    print(tiles.index(atag), ":", atag.text)
