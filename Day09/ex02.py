



import convertor as cvt

# 파일이름(모듈).함수() 
# import convertor
m1 = convertor.kilo_to_miles(100)

# import convertor as cvt
m2 = cvt.kilo_to_miles(200)

#파일(모듈) 내부의 함수를 포함
from convertor import kilo_to_miles
from convertor import gram_to_pound
from convertor import kilo_to_miles,gram_to_pound

# convertor 모듈안의 모든 함수를 포함
# * : 모든 항목
from convertor import *

