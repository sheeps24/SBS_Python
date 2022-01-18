

# math 모듈포함
import math;

#넓이
# get-area() 함수정의

def get_area( radius ):
    #def 함수명 (매개변수) :
    # (넓이) = (원주율) * r * r
    area = math.pi * math.pow(radius, 2)
    return area

# 파이썬은 코드블록을 들여쓰기로 구분.

#반지름
radius = 4
#함수 호출 : 함수명(전달인자)
area = get_area(radius)
print("area : " , area)

