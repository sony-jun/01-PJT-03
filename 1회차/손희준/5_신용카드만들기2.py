

n = int(input())
for i in range(n):
    number = input()
    n_n = []
    card_n = []
    for j in number:
        n_n.append(j)
    
    for k in n_n:
        if k =='-':
            k = ''
        else:
            card_n.append(k)
    if len(card_n) == 16 and (card_n[0] =='3' or card_n[0] =='4' or card_n[0] =='5' or card_n[0] =='6' or card_n[0] =='9'):
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')



