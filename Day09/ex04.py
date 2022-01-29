

'''

표준 모듈
1.math     : 수학 연산과 관련된 함수를 제공하는 모듈 
2.randome  : 난수(랜덤 수)를 생성하는 모듈
3.time     : 시간처리 관련한 모듈
4.datetime : 날짜/시간 데이터를 처리하는 모듈

'''


import math

print('math.pi : {}'.format(math.pi))

# ceil() 올림
print('math.ceil(1.1) : {}'.format(math.ceil(1.1)))

# floor() 내림   = 음수 방향으로 가까운 정수 반환                 # 내림과 절사는 양의 수 일땐 차이가 없지만, 
print('math.floor(1.9) : {}'.format(math.floor(1.9)))          # 음수에서는 차이가 난다.

# round() 반올림
print('math.round(2.5,1) : {}'.format(round(2.5,1)))
print('math.round(2.4,1) : {}'.format(round(2.4,1)))

# trunc() 절사 (특정 자리수 이하를 없앰)  - 0에 가까운 정수 반환
print('math.trunc(1.9) : {}'.format(math.trunc(1.9)))

# sqrt() 제곱근
print('math.sqrt(9) : {}'.format(math.sqrt(9)))

# pow() 제곱
print('math.pow(3,2) : {}'.format(math.pow(3,2)))


import random

# random() : 0.0xxx ~ 0.9xxx 임의의 실수
print('random.random : {} '.format(random.random()))

# randint(a,b) : a이상 b이하의 임의의 정수
print('random.randint : {} '.format(random.randint(1,10)))

# randrange(a,b,c) : a이상 b미만 c만큼 증가하는 임의의 정수
print('random.randrange : {} '.format(random.randrange(1,10,2)))

# choice() : 시퀀스 자료형에 속한 요소 중 임의의 요소를 반환하는 함수
seasons = ['봄','여름','가을', '겨울']
print('내가 가장 좋아하는 계절은 {} 입니다.'.format(random.choice(seasons)))

# sample() : 시퀀스 자료형에 속한 요소 중 지정한 개수의 요소를 임의의로 반환하는 함수
#             A중의 N개의 임의의 요소
lotto = range(1,46)
print('이번 주 당첨 번호는 {} '.format(random.sample(lotto, 6)))

# shuffle(A) : 시퀀스 자료형에 속한 요소들의 순서를 임의로 섞는 함수
#             A의 요소들의 요소를 섞는다

li = [1,2,3,4,5]
random.shuffle(li)
print('random.shuffle(li) :  {} '.format(li))







