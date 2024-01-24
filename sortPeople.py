def sortPeople(names,heights):
    names_heights = {}
    result=[]
    for i in range(0,len(names)):
        names_heights[heights[i]]=names[i]
    sorted_names = sorted(names_heights.keys())

    for i in range(len(sorted_names)-1,-1,-1):
        result.append(names_heights[sorted_names[i]])
    return result


print(sortPeople(["Mary","John","Emma"],[180,165,170]))

