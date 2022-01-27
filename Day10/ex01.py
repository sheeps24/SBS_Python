

'''
    파일 입출력
    
    - 텍스트 파일 생성하기
'''
# 파일 저장 경로
path = 'C:/박상우/SBS_PYTHON/SBS_Python/Day10/'

# 파일 열기 : open( (경로) + 파일명, 모드, 옵션 )
file = open(path + 'hello.txt','wt',encoding='UTF-8')  # 경로가 너무 길어 변수로 입력 후 붙임

# 파일 내에서 출력 : write()
file.write('안녕하세요')
file.write('\n')
file.write('파일 입출력 내용을 학습.')
print('파일이 생성되었습니다.')

file.close() 


# file.close ()






















'''
파일 객체=open(파일명,모드)
open('sample.txt')

파일면 작성
1.open('sample.txt')
2.open('C:/sample.txt')
3.open()


open('sample.txt','wt')
:현재 경로에서 sample.txt 파일을 쓰기ㅣ모드의 텍스트파일을 열기

파일 닫기
close() : 더 이상 사용하지 않는 파일을 프로그램에서 종료

'''



