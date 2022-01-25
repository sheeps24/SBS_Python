

'''
다중 반환 
    : 파이썬에서는 하나의 반환값도 처리 할 수있고,
    여러개의 반환값도 처리할 수있다

def 함수명(매개변수):
    실행문
    실행문
    return (값1),(값2),(값3), ...
    
'''


def cal (*args):
    result1 = sum(args)
    result2 = sum(args)/len(args)
    result3 = max(args)
    result4 = min(args)
    return result1,result2,result3,result4   # return은 언제 쓰이는가?
    # 반환값들을 튜플로 생성하여 반환

a,b,c,d = cal(1,2,3,4,5)  # (15,3,5,1) or (15),(3),(5),(1) ??
result = cal(1,2,3,4,5)

print('a : {}'.format(a))
print('b : {}'.format(b))    
print('c : {}'.format(c))
print('d : {}'.format(d))

print('result : {} '.format(result))


'''
def c_m(money,coffee):
    print('{}을 선택하시고, {}원을 지불하셨습니다.'.format(coffee,money))
    
    m = { '요거트' : 5000,
          '생딸기 프라페' : 5600,
          '초코 라떼' : 4900
        }
    
    if coffee not in m:   
        print('선택하신 {}는 메뉴에 없습니다.'.format(order)) # coffee?
        return money,'없는 메뉴'
    elif pay < m[order]:
        print('잔액 부족. 선택하신 {}는 {}원 입니다.'.format(order,m[order]))
        return money,'잔액부족'
    else:
        print('주문하신 {} 나왔습니다.'.format(order))
        return money - m[order],order
    
    
order = input('메뉴를 선택하세요 : ')
pay = input('지불 하실 금액 :')
pay = int(pay)

a,b = c_m(pay,order)
print('잔액은 {} 입니다. 커피 : {}'.format(a,b))


# 여기서 인수와 매개변수의 차이는?

'''