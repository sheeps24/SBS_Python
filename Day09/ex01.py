

#모듈
'''
모듈이란?
: 변수나 함수또는 클래스로 모아놓은 파이썬 파일
  - 하나의 파이썬 파일(.py)
  
패키지?
: 모듈들이 여러 개 모여있는 폴더

모듈의 사용
: import 모듈

'''

import convertor
from convertor import *

miles = kilo_to_miles(150)
print('150Km = {} miles'.format(miles))


pound = gram_to_pound(1000)
print('1000g = {} pound'.format(pound))



