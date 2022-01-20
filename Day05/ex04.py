

#논리 연산
# and : A and B 와 같은 조건에서 ,
#       A,B 모두 True or False  일때, 결과는 True or False이다.

# or : A or B 와 같은 조건에서 ,
#       A와B 둘 중 하나라도 True면, 결과는 True이다.

# not : True면 False로,False면 True로 됨.


a = 10
b = 5
print('{} > 7 and {} > 7 = {}' .format(a,b,a > 7 and b > 7))
print('{} > 7 or {} > 7 = {}'.format(a,b,a > 7 or b > 7))


print('not{} : {}'.format(a,not a))
print('not{} : {}'.format(0,not 0))
