#세트
# : 집합의 개념
# 중복없이 순서가 없는 여러개의 데이터를 저장하는 컬렉션
# - 중복된 값을 제거하거나, 교집합, 합집합등의 개념이 필요한 경우 사용
# - 기호 : {}
# - s ={값1, 값2}
 
s1 = {1,2,3,4,5}
print('s1 :' , s1)

# 순서존재 x 인덱싱 불가

#세트의 요소 추가 및 삭제
# 추가 : add()
# 삭제 : remove(), discard()

s1.add(7)
print(s1)

s1.add(8)
print(s1)

# 중복값을 추가안함

s1.add(7)
print(s1)

#세트에서 값을 찾아 삭제
s1.remove(8)
print(s1)

s1.discard(7)
print(s1)

# remove와 discard의 차이
# s1.remove(10) -에러
# remove는 없는 값을 삭제할때 에러발생
print(s1)

s1.discard(10)
print(s1)

