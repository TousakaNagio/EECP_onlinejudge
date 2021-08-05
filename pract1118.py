def Sum(A):
    total = 0
    for i in A:
        if type(i) == int:
            total += i
        elif type(i) == list:
            total = total + Sum(i)
    return total
    pass

def Digit_Sum(B):
    total = 0
    for i in B:
        if type(i) == list:
            total += Digit_Sum(i)
        else:
            if type(i) == int:
                total += digit_sum_int(i)
            elif type(i) == float:
                total += digit_sum_float(i)
    return total
    pass

def digit_sum_int(x):
    sum_ = 0
    while(x!=0):
        sum_ += x%10
        x = x//10
    return sum_
    pass

def digit_sum_float(y):
    sum_ = 0
    while int(y)!=y:
        y = y * 10
    sum_ = sum_ + digit_sum_int(y)
    return int(sum_)

def test(z):
    z = z+2
    print(z)

if __name__ == "__main__":
    q = [1.2,2,3,4.12345,[5,6,[7,8,9,[10,11.12345],12,13],14],15,16,17,18]
    print(Digit_Sum(q))
    d = 3
    test(3)
    print(d)
    a = [2,3]
    b = a
    b.append(4)
    print(a)