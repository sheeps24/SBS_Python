

# 파일 저장 경로
path = 'C:/박상우/SBS_PYTHON/SBS_Python/Day10/'

# 읽기 모드 : r  (read)
# 파일 유형 : t  (text)
file = open(path + 'hello.txt','rt', encoding='UTF-8')

while True:
    # str = file.read(10)    # 파일로부터 10글자씩 읽어온다.
    str = file.readline()    # 파일로부터 한줄 씩 읽어온다.
    if not str:              # 읽어온 글자가 없으면, 중지
        break
    print(str, end='')
    
file.close()