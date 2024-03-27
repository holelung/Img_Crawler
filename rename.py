import os

# 바꿀 파일이름
change = "rose"
# 파일 경로
file_path = f'/Users/jangjunho/develop/Python_Crawling/{change}'

file_names = os.listdir(file_path)
file_names.sort()  # 파일 이름을 알파벳 순으로 정렬

for i, file in enumerate(file_names, start=1):  # 인덱스를 1부터 시작
    src = os.path.join(file_path, file)
    dst_name = f"{change}_{i}.jpg"
    dst = os.path.join(file_path, dst_name)
    os.rename(src, dst)
