

import time

# 파일 저장 경로
path = 'C:/박상우/SBS_PYTHON/SBS_Python/Day10/'

today = time.strftime('%Y-%m-%d')

# 파일 열기 : open( (경로) + 파일명, 모드, 옵션 )
file = open(path + '할일(' + today + ')' + '.txt', 'wt', encoding='UTF-8')

no =1
while True:
    todo = input('오늘 할일 : ')
    
    #아무 값도 입력하지 않은 경우 - 종료 
    if not todo:
        break
    
    file.write(str(no) + ' ' + todo + '\n')
    no += 1

file.close
