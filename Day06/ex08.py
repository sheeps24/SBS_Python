



# 단을 입력받아서 구구단을 출력
#구구단 출력하기
dan = input("단 :")
dan = int(dan)
for n in range(1,10):
    print(' {} X {} = {}' .format(dan, n, dan*n))