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
      <a href="https://www.naver.com">네이버로 이동</a>
    </li>
    <li>
      <a href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a href="https://www.daum.net">다음으로 이동</a>
    </li>
  </ul>
</nav>
"""

# HTML 파싱
bs = BeautifulSoup(html, 'html.parser')

a_tags = bs.select('a')
a_tag = bs.select_one('a')
print(a_tag)

# for tags in a_tags:
#   print(tags.get_text())