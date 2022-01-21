


# 대한민국의 수고를 맟추는 퀴즈

#무한 반복
# 무조건 계속 반복하는 반복문
# 반드시, 종료조건을 넣어야한다.

while True:
    city = input('대한민국의 수도는? ')  # --> 밖에다 빼면??
    #종료 조건
    if city == '서울' or city == 'seoul':       #--> =는 안되나??   
        print('정답입니다.')                    # or city를 안넣으면?
        break
    else:
        print('오답입니다.')