from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 사용자 에이전트 설정 (모바일 환경으로 설정)
user_agent = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

# 크롬 옵션 설정
options = Options()
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 설정 및 실행
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 멜론 모바일 페이지 접속
url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(1)  # 페이지 로드 대기

# 이벤트 페이지를 감지하고 넘어가는 함수 정의
def check_and_pass_event_page():
    try:
        event_banner = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ir-pm'))
        )
        melon_logo = driver.find_element(By.XPATH, '/html/body/div[2]/header/h1/a/img')
        melon_logo.click()
    except:
        pass

check_and_pass_event_page()

# 차트 항목 클릭
chart_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="naviMenu"]/nav/ul/li[3]/a'))
)
chart_link.click()

# 스크롤을 통해 페이지 끝까지 로드하는 함수 정의
def scroll_down_inf():
    prev_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == prev_height:
            break
        prev_height = new_height

scroll_down_inf()

def click_load_more():
    button_selector = "#moreBtn"
    driver.execute_script("hasMore2();")
click_load_more()

click_load_more()
scroll_down_inf()

# 데이터 추출
chart_list = driver.find_element(By.ID, '_chartList')
list_item = chart_list.find_elements(By.CLASS_NAME, 'list_item')

for item in list_item:
    rank = item.find_element(By.CLASS_NAME, 'ranking_num').text.split()[0]
    title = item.find_element(By.CLASS_NAME, 'content').find_element(By.TAG_NAME, 'p').text
    artist = item.find_element(By.CLASS_NAME, 'content').find_element(By.TAG_NAME, 'span').text
    print(f'순위: {rank}, 노래 제목: {title}, 가수 이름: {artist}')

# 브라우저 종료
driver.quit()