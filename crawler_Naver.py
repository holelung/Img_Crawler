from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
import os


# 검색어 입력
search_term = "코스모스"
# 저장 폴더 입력
path_folder = f'/Users/jangjunho/develop/Python_Crawling/{search_term}'

# Chrome 드라이버 실행
driver = webdriver.Chrome()
driver.get("https://www.naver.com")
time.sleep(3)

# 검색 입력 및 실행
box = driver.find_element(By.ID, 'query')
box.send_keys(search_term)
box.send_keys(Keys.ENTER)

# 이미지 탭 클릭
box_img = driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a' )
box_img.click()
time.sleep(3)

# 스크롤 전 이미지 수
prev_img_count = 0
last_height = driver.execute_script("return document.body.scrollHeight")


# 결과 로딩 대기
time.sleep(3)  # 로딩 시간을 위해 대기, 필요에 따라 조절



if  not os.path.isdir(path_folder):
    os.mkdir(path_folder)

# 이미지 URL 수집
urls = []

while True:
    
    # 페이지 끝까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 새 이미지 로드를 기다림
    new_height = driver.execute_script("return document.body.scrollHeight") 
    # 이미지 Class 입력
    images = driver.find_elements(By.CSS_SELECTOR, "img._fe_image_tab_content_thumbnail_image")

    
    if new_height == last_height:  # 새 이미지가 로드되지 않으면 종료
        try:
            more_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input'))
            )
            more_button.click()
             
            time.sleep(2)
        except Exception as e:
            print("더보기 버튼을 찾거나 클릭할 수 없습니다.", e)
            break
        
    else:
        last_height = new_height ##last_height update

    # 새로 로드된 이미지 URL 수집
    for image in images:
        url = image.get_attribute('src') or image.get_attribute('data-src')
        if url and 'http' in url and url not in urls:  # 중복 확인
            urls.append(url)


# 이미지 다운로드
print("이미지 다운로드 시작")
for i, url in enumerate(urls):
    urllib.request.urlretrieve(url, f"./{search_term}/{search_term}_{i}.jpg")


print("종료")
driver.close()



