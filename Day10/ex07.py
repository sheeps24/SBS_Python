

'''
   CSV (Comma Saparated Value)
   : 콤마(,)로 분리한 값들
   
   ex) 
        학번,이름,주소,전화번호
        101,김철수,서울시 노원구, 010-1234-1234
        102,김철수,서울시 노원구, 010-1234-1234
        103,김철수,서울시 노원구, 010-1234-1234
        104,김철수,서울시 노원구, 010-1234-1234
        
'''


import csv

with open('test.csv','w',newline ='') as file:
    # delimiter : 구분기호
    csv_maker = csv.writer(file, delimiter=',' )
    csv_maker.writerow(['학번', '이름', '주소','전화번호'])
    csv_maker.writerow(['101', '김철수', '서울시 노원구', '010-1111-2222'])
    csv_maker.writerow(['102', '김철수', '서울시 노원구', '010-1111-2222'])
    csv_maker.writerow(['103', '김철수', '서울시 노원구', '010-1111-2222'])

print('파일이 생성되었습니다')
