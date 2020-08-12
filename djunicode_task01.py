def check (first,last):
    present = {}
    for i in range (first, last):
        temp = 1
        b = 0
        t = i
        while i != 0:
            r = i % 2
            i = i//2
            b = b + r*temp
            temp = temp*10
        present[t]=b
    for x in present:
        bs=str(present[x])
        if '11' in bs:
            present[x] = True
        else:
            present[x] = False
    print(present)
takein = input().split(',')
check(int(takein[0]),int(takein[1]))

