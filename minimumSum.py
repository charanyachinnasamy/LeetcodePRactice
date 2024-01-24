def minimumSum(num):
    num=str(num)
    digit_list=[int(num[digit]) for digit in range(0,len(str(num)))]
    digit_list.sort()
    result=(digit_list[0]*10+digit_list[2])+(digit_list[1]*10+digit_list[3])

    return result



print(minimumSum(1345))





