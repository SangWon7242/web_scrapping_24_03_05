import requests
from bs4 import BeautifulSoup

# 웹페이지 URL 설정
url = 'https://www.naver.com/'

# GET 요청 보내기
resp = requests.get(url)

html = """
<nav class="menu-box-1" id="menu-box">
  <ul>
    <li>
      <a class="menu-item-text" href="https://www.naver.com">네이버로 이동</a>
    </li>
    <li>
      <a class="menu-item-text" href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a class="menu-item-text" href="https://www.daum.net">다음으로 이동</a>
    </li>
  </ul>
</nav>
<div id="box"></div>
"""

# HTML 파싱
bs = BeautifulSoup(html, 'html.parser')

# find_all : 조건과 일치하는 모든 요소의 리스트
# 해당 엘리먼트의 클래스 이름으로 접근
menu_item_text = bs.find_all('a', class_="menu-item-text")

'''
for el in menu_item_text:
  print(el.get_text())
'''

menu_box = bs.find_all('nav', id="menu-box")

# find : 조건과 일치하는 첫 번째 요소
box = bs.find('div', id="box")
# print(menu_box)
print(box)


