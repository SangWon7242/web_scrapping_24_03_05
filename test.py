import requests
from bs4 import BeautifulSoup

# 웹페이지 URL 설정
url = 'https://www.naver.com/'

# GET 요청 보내기
resp = requests.get(url)

# 네이버 뉴스 url
url = 'https://news.naver.com/section/103'

# resp : response의 약자
# 지정 웹 사이트의 get요청을 보내서
# requests를 이용해 웹 페이지의 html 문서 내용 가져오기
resp = requests.get(url)

# 웹 페이지의 HTML 내용을 BeautifulSoup 객체로 변환
bs = BeautifulSoup(resp.text, 'html.parser')

new_title = bs.find_all('a', class_='sa_text_title')

new_title_list = []

for title in new_title:
  new_title_list.append(title.get_text())  

# 뉴스 제목 안에 있던 \n 을 제거하는 코드    
cleaned_news_tit = [item.replace('\n', '') for item in new_title_list]

for idx, tit in enumerate(cleaned_news_tit):
  print(f"{idx + 1} : {tit}")
  
# 해당 키워드로 리스트 순회 후 찾은 내용을 
# keyword_tit_list 에 저장
keyword = '봄'  
keyword_tit_list = []
for tit in cleaned_news_tit:
  if keyword in tit:
    keyword_tit_list.append(tit)

print(keyword_tit_list)    
