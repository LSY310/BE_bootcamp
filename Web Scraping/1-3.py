import requests
from bs4 import BeautifulSoup

# 웹 스크래핑을 위해 사용자 에이전트를 설정
header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

# CGV 영화 목록 페이지 URL
url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

# requests 라이브러리를 사용하여 웹 페이지를 요청
req = requests.get(url, headers=header_user)

# 웹 페이지의 HTML 소스를 가져옴
html = req.text

#BeautifulSoup을 사용하여 HTML 소스를 파싱하고 필요한 데이터를 CSS 선택자를 사용하여 추출
soup = BeautifulSoup(html, "html.parser")

rank = soup.select(".rank")
title = soup.select(".title")
percent = soup.select(".percent > span")
txt = soup.select(".txt-info")

# zip 함수를 사용하여 각 영화의 정보를 묶어서 출력
for i in zip(rank,title,percent,txt):
    print("영화 순위 :",i[0].text)
    print("영화 제목 :",i[1].text)
    print("예매율 :",i[2].text)
    print("개봉일자 :",i[3].text.split()[0])
    print(sep="/")
