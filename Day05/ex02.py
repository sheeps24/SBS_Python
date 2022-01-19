

bank = 0    #저금통

money = 10000

# bank = bank + money
bank += money
print('통장에 돈을 {} 원 넣었습니다.'.format(money))
print('통장에 돈이 {} 원 있습니다.'.format(bank))

snack = 2000

bank -= snack  # bank = bank - snack
print('{}짜리 과자 구입했습니다.'.format(snack))
print('통장에 돈이 {} 원 있습니다.'.format(bank))