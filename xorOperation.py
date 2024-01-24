def xorOperation(n,start):

    result=0
    for i in range(0,n):

        result=result^(start+2*i)
    return result

print(xorOperation(4,3))


