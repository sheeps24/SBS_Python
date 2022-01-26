

'''

개인정보를 마스킹하는 함수를 정의
김*수, 김**, 19990101-1******  

'''

def secure_name(name):
    return name[0] + '**'

def secure_no(no):
    return no[0:8] + '******'

def secure_phone(phone):
    return phone.replace(phone[4:8],'****')


    