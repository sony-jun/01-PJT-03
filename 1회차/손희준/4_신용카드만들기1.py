

n = int(input())
for i in range(n):
    number = list(map(int,input().split()))
    cnt = []
    for j in range(len(number)):
        if j % 2 == 0:
            cnt.append( 2*number[j])
        else:
            cnt .append( number[j])
    sixteen = (10 - sum(cnt)%10)%10
    print(f'#{i+1} {sixteen}')


