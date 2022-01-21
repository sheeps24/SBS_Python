


eng_dict ={
    'sun' : '태양',
    'moon' : '달',
    'star' : '별',
    'space' : '우주'
}


for word in eng_dict:
    print('{}의 뜻 : {}' .format(word, eng_dict.get(word)))
    
    # 딕셔너리.get(key) : key에 해당하는 값을 가져온다.
    # word는 키값을 가져옴.