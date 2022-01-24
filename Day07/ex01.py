


# 내장 함수
# : 외부에 따로 정의한 모듈에 있는 함수가 아닌
#   파이썬 내부에 내장되어있는 함수
#   바로 사용 가능한 함수


# 문자열 내장 함수
'''
(참조) 모든 문자는 각 문자 코드를 가지고 있음.
1. chr() 함수
: 특정 문자의 유니코드 값을 입력하면,
  해당 문자를 반환하는 함수
  
2. ord() 함수
: 특정 문자를 입력하면,
  해당 문자의 유니코드를 반환하는 함수 # chr과 반대
  
3. eval() 함수
: 표현식을 문자열ㄹ로 입력하면 표현식의 결과를 반환하는 함수
   ex) eval('100 + 200')  --> 300
       a = 10
       eval ('a' * 5 ) --> 50

4. format() 함수
: 전달 받은 값과 포맷코드에 따른 형식 문자열을 반환하는 함수
  ex) 1,000,000
      format(1000000, ',') --> 1,000,000   
      
5. str() 함수
: 전달받은 인수를 문자열로 변환하는 함수 
ex) str(10)  --> '10'
'''

# chr
print(chr(97)) 
print(chr(98))
print(chr(99))
print(chr(100))

# ord
print(ord('a')) 
print(ord('b'))
print(ord('c'))
print(ord('d'))

# eval 
expr = input("입력 : ")
result = eval(expr)
print('결과 : '+ str(result))


# format
print(format(1000000, ','))

# str
print(str(1.5))