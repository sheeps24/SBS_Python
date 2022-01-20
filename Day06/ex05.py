

# for 반복문
# for 변수 in (리스트 , 튜플 등 컬렉션)
li = [1,2,3,4,5]

for n in li:
    print(n, end=' ')
    
    
# 문자열을 입력받아 비번을 확인하는 프로그램
# 비밀번호 조건 : 숫자, 문자 모두 포함
print()
pwd = input('비밀번호 : ')

ch_count = 0  #문자의 개수
num_count = 0  #숫자의 개수

# pwd라는 문자열을 한 글자씩 가져와 반복
for ch in pwd:
    #isalpha() : 해당 문자가 알파벳이면 True
    #isnumeric() : 해당 문자가 숫자면 True
    if ch.isalpha():
        ch_count += 1
    if ch.isnumeric():
        num_count +=1
#        
if ch_count > 0 and num_count > 0:
    print('사용 가능한 비번')
        
else:
    print('사용 불가능한 비번')
        
            