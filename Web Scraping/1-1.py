import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 하나만 입력해주세요")

url = base_url + keyword
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

#여기서 부터 코드를 작성해주세요
# 광고 배너의 id 또는 class 명을 찾아보세요
# 광고 배너의 결과값을 변수 담아서 if문으로 검증을 합니다.
# 아무것도 없는 경우는 어떤 값이 들어가는지 확인해주세요
# if문의 참과 거짓일 경우 어떻게 작동하는지에 대한 원리를 상기시켜보세요

blog = soup.select(".user_info > a")
title = soup.select(".title_area")
users = soup.select(".user_box")# 큰상자

for user, names, name in zip(users, title, blog):
    if user.find(class_="spblog ico_ad"):
        continue
    else:
        print(f" 저자 : {name.text}")
        print(f" 제목 : {names.text}")
        print(sep="/")