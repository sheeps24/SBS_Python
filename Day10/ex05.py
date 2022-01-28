

# 파일 삭제
# os 모듈에 파일 삭제 기능이 정의되어있다.


import os

# 파일 저장 경로
path = 'C:/박상우/SBS_PYTHON/SBS_Python/Day10/'


file = input('삭제 파일명 : ')
file = path + file  # file = path + 'hello.txt'


if os.path.exists(file):  # 파일의 존재 확인
    os.remove(file)
    print('파일이 삭제 되었습니다.')
    
    
