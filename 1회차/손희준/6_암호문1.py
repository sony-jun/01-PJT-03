for t in range(1, 11) :
    N = int(input())
    code = list(map(int, input().split()))
    M = int(input())
    instruction = list(input().split())

    ins = []
    for i in range(len(instruction)) :
        if instruction[i] == "I" :
            if i != 0 :
                ins.append(tmp)
            tmp = []
        elif i == len(instruction)-1 :
            tmp.append(int(instruction[i]))
            ins.append(tmp)
        else :
            tmp.append(int(instruction[i]))

    for i in range(M) :
        x = ins[i][0]
        y = ins[i][1]
        s = ins[i][2:]
        for j in range(y) :
            code.insert(x+j, s[j])

    print("#{} {} {} {} {} {} {} {} {} {} {}".format(t, *code))


# 답을보고 나서 생각한건데 이 당시에는 내가 못푸는 문제가 아니였나...
# 실력의 부족을 통감했음


