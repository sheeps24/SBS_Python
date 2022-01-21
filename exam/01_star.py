

'''
   제어문(조건문,반복문을) 이용하여, 
   아래와 같이 * 문자로 이루어진 도형을 출력하는 
   프로그램을 완성해라.
   
   1)
   숫자 N을 입력받아 N행의 줄에 다음과 같이 
   삼각형 모양을 만들어라
   
   *
   **
   ***
   ****
   *****
   
   2) N : 5
       *
      ***
     *****
    *******
   *********
   
   
'''

# 1)
a = '*'
b = 1

while b <= 5 :
    print(a)
    a += '*'
    b += 1
    
# 2)
a = '*'
b = ' '
c = 1

while c <= 5:
    if c == 1:
        print(b*3, a, b*4)
    elif c == 2:
        print('   ***   ')
    elif c == 3:
        print('  *****  ')
    elif c == 4:
        print(' ******* ')
    elif c == 5:
        print('*********')
    c += 1
    
#3)

a = input("정수 입력 : ")
a = int(a)
b = 0 
while a > 0 :
    while b < a:
        c += b
    b += 1
            
print('합계 : {}'.format(a+c))