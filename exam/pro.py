


# 1단계

# 입력 받은 수 N 만큼 줄이 반복
# N번째 줄의 크기만큼 병릐 개수 반복

N = input('N : ')
N = int(N)

# i : 0,1,2,3,4
for i in range(0,N):
    for j in range(0,i+1):
        print('*',end = "")
    print()
    
    
# 2단계
# N : 5
# i : 1,2,3,4,5

for i in range(1, N+1):
    # N-i : 4,3,2,1,0
    for j in range(N-i) :
        print(' ', end='')
    for j in range(1,i*2):
        print()
          