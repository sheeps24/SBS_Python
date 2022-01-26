


'''
1. 지역변수
: 함수 내부에서 선언한 변수
  함수 내부에서만 접근 가능하고, 외부에서는 접근 할 수 없다.

2. 전역변수
: 함수 외부에서 선언한 변수
  함수 내부나 외부 모든 영역에서 접근 할 수 있다 



'''

def func():
    a = 10  #지역변수
    print('f() 내부 - a : {}'.format(a))

# print('f()) 외부 - a : {}' .format(a))
# 에러 발생
# NameError: 'a' is not defined

func()      #함수 호출


b = 10     #전역변수

def test():
     print('f() 외부 - b : {}' .format(b))
     
test()     #함수 호출
print('f() 외부 - b : {}' .format(b))