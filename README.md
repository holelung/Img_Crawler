# Img_Crawler

11번째줄 검색어 입력 칸에 검색어 입력 후 실행


# 민구를 위한 튜토리얼!

1. 첫번째 파일을 다운받는다.

2. 두번째 
 * vscode에서 폴더를 연 뒤 ctrl + shift + P 를 누른다
 * 파이썬 환경만들기를 선택한다.
 * Conda를 누르고 3.11 버전을 선택한다.

3. 세번째
```
pip install selenium
```
터미널에 친다 절대 **powershell**로 하지말것

4. test.py의 11번째 줄
```
# 검색어 입력
search_term = "**검색어 여기 입력**"
# 저장 폴더 입력
path_folder = f'**파일경로 여기 입력**\{search_term}'

# 이미지 다운로드
print("이미지 다운로드 시작")
for i, url in enumerate(urls):
    urllib.request.urlretrieve(url, f"./{search_term}/{search_term}_{i}.jpg")
```
 * "sunflower" 부분을 수정한다.
 * path_folder 의 ''부분을 절대경로로 수정하고 마지막에 \{search_term} 을 꼭 붙인다(윈도우기준)
 * user가 한글일 경우 C드라이브에 폴더를 만들어 경로를 설정한다.
 * 이미지 다운로드 부분의 경로를 \(역슬래시)로 바꿀것.

 
 