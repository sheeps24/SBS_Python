


import time  # as t

# 
print('time() : {}'.format(time.time()))

t = time.time()
print('ctime() : {}'.format(time.ctime(t)))

'''
날짜 지시자 
%y    : 2자리 년도(22)
%Y    : 4자리 연도(2022)
%m    : 2자리 월(01~12)
%b    : 3자리 영문 월(Jan ~ Dec)
%B    : 전체 영문 월 
%d    : 2자리 일(01~31)
%a    : 3자리 요일(Sun ~ Sat)
%A    : 전체 영문 요일
%I    : 12 시간(1~12)
%H    : 24 시간(00~23)
%M    : 분 (00~59)
%S    : ch (00~59)
''' 

s = time.strftime('%Y/%m/%d (%a) %H/%M/%S')
print('strftime() : {}'.format(s))

#지정한 시간(초)만큼 시스템을 일시중지
time.sleep(5) #5초간 정지

import datetime

#[모듈].[객체].now()
nowtime = datetime.datetime.now()
print('현재 날짜와 시간 : {}'.format(nowtime))

today = datetime.date(2022,1,13)
print('현재 날짜와 시간 : {}'.format(today))

specialDay = datetime.date(2022,2,7)
print('종강일 : {}'.format(specialDay))

t1 = datetime.time()
print('현재시간 : {}'.format(t1))

t2 = datetime.time(15,50,0)
print('수업종료 : {}'.format(t2))

today = datetime.datetime.now()
print('{} 년'.format(today.year))
print('{} 월'.format(today.month))
print('{} 일'.format(today.day))
print('{} 시'.format(today.hour))
print('{} 분'.format(today.minute))
print('{} 초'.format(today.second))






 