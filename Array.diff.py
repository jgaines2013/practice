def array_diff(a, b):
    #your code here
    newList = []
    # contains = b in a //not needed but interesting
    for i in range(len(a)):
        if a[i] not in b:
            newList.append(a[i])
    return newList


# discovered new cleaner way
# return newList = [a[i] for i in range(len(a)) if a[i] not in b]
#            ^
#            | this element gets appended(used/compared)
