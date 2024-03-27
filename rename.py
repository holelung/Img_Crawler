import os

# 변경할 파일
flower = "sunflower"
# 변경할 파일 경로
file_path = f'/Users/jangjunho/develop/Python_Crawling/{flower}'

file_names = os.listdir(file_path)
file_names.sort()  # 파일 목록을 알파벳 순서로 정렬

for i, file in enumerate(file_names, start=1):  # enumerate를 사용하여 인덱스와 파일 이름을 얻음, 인덱스는 1부터 시작
    src = os.path.join(file_path, file)
    dst_name = f"{flower}_{i}.jpg"
    dst = os.path.join(file_path, dst_name)
    if not os.path.exists(dst):  # 동일한 이름의 파일이 존재하지 않는 경우에만 이름 변경
        os.rename(src, dst)
    else:
        print(f"파일 이름 '{dst}'은(는) 이미 존재합니다.")
