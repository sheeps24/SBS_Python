


'''
시퀀스 내장 함수

1. enumerate() 함수
   : 리스트와 함께 사용하여,
    (index,튜플)의 형태로 반환하는 함수
   ex) for item in enumerate(['a','b','c'])
        print(item)
    (결과)
    (0, 'a')
    (1, 'b')
    (2, 'c')
    
2. range() 함수 
   : 전달 받은 값에 따라서 특정 범위에 데미터를 반환하는 함수
   
   i) ramge(끝)
   
   ii)range(시작,끝)
   
   iii)range(시작,띁,단계)
   
3. len() 함수
    : 함수에 전달된 객체의 길이를 반환하는 함수
    ex) li = [1,2,3,4]
        len(li)  --> 4
        
4. sorted() 함수
    : 반복 가능한 객체를 오름차순우로 정렬한 결과르 반환하는 함수
    ex) li = [10,3,9,2,5]
        sorted(li) --> [2,3,5,9,10]
        
5. zip() 함수
    : 여러 개의 반복가능한 객체들을 튜플로 묶어 반환하는 함수
    ex) names = ['c언어', '파이썬', 'JAVA']
        score = [100, 90, 80]
        zip(name,score) 
        --> ( 'c언어' , 100  )
            ( '파이썬' , 90  )
            ( 'JAVA' , 80  )           
            
'''

#c언어 , 파이썬, JAVA
# 0, 1, 2
# enumerate(prog)

prog = ['c언어', '파이썬', 'JAVA']
for item in enumerate(prog):
    print(item)

print()    


# range(1,11)    
for i in range(1,11):
    print(i, end = ' ')

print()

# range(2,21,2)
for i in range(2,21,2):
    print(i, end = ' ')
    
print()


li =  ["월", "화", "수", "목", "금" , "토",  "일"]
print(li)
print('li의 요소의 개수 : {} '.format(len(li)))


scores = [100, 90, 65, 80, 70]
print(scores)
print( sorted(scores) )

names = ['s1','s2','s3','s4','s5']  

for student in zip(names,scores):
    print(student)  
    

