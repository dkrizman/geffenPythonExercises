def sortList(lst=[]):
    breakFlag = False
    if type(lst)!=list:
        print('input not a list')
        breakFlag = True
    intFlag = True
    for i in lst:
        if type(i)!=int:
            intFlag = False
    if not intFlag and not breakFlag:
        print('not all instances are integers')
        breakFlag = True
    if not breakFlag:
        sortedList = [0]*len(lst)
        minTemp = 0
        for i in range(len(lst)):
            for j in range(len(lst)):
                if i!=j and lst[j]>=lst[i]:
                    minTemp = lst[j]
                    lst[j] = lst[i]
                    lst[i] = minTemp
        return lst

def isSorted(l1):
    flag = True
    for i in range(len(l1)-1):
        if l1[i] > l1[i+1]:
            flag = False
            break
    return flag


def mergeSorted(l1, l2):
    if not isSorted(l1) or not isSorted(l2):
        print('one or more input list werent sorted and we sorted it for you')
        l1 = sortList(l1)
        l2 = sortList(l2)
    else:
        res = []
        index2 = 0
        index1 = 0
        for i in range(len(l1)+ len(l2)):
            if index1<len(l1):
                if l1[index1] <= l2[index2]:
                    res.append(l1[index1])
                    index1 += 1
            elif index2 < len(l2):
                res.append(l2[index2])
                index2 += 1
    return res


l1 = [1,2,3,4]
l2 = [3,5,6,7]
mergeSorted(l1, l2)