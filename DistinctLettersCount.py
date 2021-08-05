def solution(S):
    l = len(S)
    s = set(S)
    if len(s)==1:
        return 0
    a = []
    for i in s:
        count = 0
        for j in S:
            if j==i:
                count += 1
        a.append(count)
    b = sorted(a)
    b.reverse()
    c = list(set(b))
    if len(b)==len(c):
        return 0
    if len(b)>len(c):
        count = 0
        for i in c:
            b.remove(i)
        for i in range(len(b)):
            while b[i] in c and b[i]!=0:
                b[i] -= 1
                count +=1
            if(b[i]>0):
                c.append(b[i])

    return count
    pass

if __name__ == "__main__":
    q = input()
    if q =='_':
        q=''
    print(solution(q))

