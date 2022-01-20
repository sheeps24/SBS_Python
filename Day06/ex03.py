# 조건문

# �ݺ��� 
# : ������ ������ �� ����, ���๮�� �ݺ��ϴ� ����
# while��
# while ���ǽ� :
#     �ݺ� ���� ����
# for��
# for ���� in(�ݺ������� ��ü)
#     �ݺ� ������ ����



i = 1
while i <= 10:
    print(i , end =' ')
    i = i + 1
    
# 1~10 까지의 합계
    sum =0
    a = 1
while a <= 10:
    sum += a
    print(a, end ='')
        
    if( a!= 10 ):
        print('+' , end=' ')
            
        a = a + 1
print()
print('sum = {}'. format(sum))