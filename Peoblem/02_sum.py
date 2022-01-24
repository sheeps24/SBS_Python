
'''
    정수 하나를 입력받아,
    1부터 입력받은 수까지의 합계를 구하는 프로그램을 완성하시오.
    (입력예시) N : 10
    (출력예시) 합계 : 55
'''

N = input("정수 : ")
N = int(N)
sum = 0

for i in range(1,N+1):
    sum = sum + i
    if N != 10:
        print(i , end = '+')
    elif N == 10 : 
        print(i, end ='=')
    
print("합계 : {}".format(sum))


'''
a = input('정수 입력: ')
a = int(a)
c = 1
b = 1
while c <= a:
    print( '*' * b )   
    b += 1 
    c += 1 ''' 
'''
a = input('입력 :')
a = int(a)
c = 1

while c < a:
    b = 0
    for i in range(1,a):
        b += i
    c += 1
    
print('합 = {}'.format(a+b))
'''