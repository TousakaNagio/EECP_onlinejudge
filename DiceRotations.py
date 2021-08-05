def solution(A):
    # write your code in Python 3.6
    # you only need to modify this function
    a = [1,6]
    b = [2,5]
    c = [3,4]
    total = []
    #if [x for x in a if x in A] == a:
    for i in range(1,7):
        count = 0
        for x in A:
            if i==1 and x in b+c:
                count += 1
            elif i==1 and x==6:
                count += 2
            if i==2 and x in a+c:
                count += 1
            elif i==2 and x==5:
                count += 2
            if i==3 and x in b+a:
                count += 1
            elif i==3 and x==4:
                count += 2
            if i==4 and x in b+a:
                count += 1
            elif i==4 and x==3:
                count += 2
            if i==5 and x in a+c:
                count += 1
            elif i==5 and x==2:
                count += 2
            if i==6 and x in b+c:
                count += 1
            elif i==6 and x==1:
                count += 2
        total.append(count)
       
    return min(total)
    pass

if __name__ == "__main__":
    q = [int(i) for i in input().split(',')]
    print(solution(q))

