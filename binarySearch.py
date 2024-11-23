def binary_search(l,v):
    left = 0
    right = len(l) - 1
    m = 0


    while left <= right:
        m = (left + right) // 2
        mv = l[m]

        if mv == v :
            return m

        if mv < v:
            left = m + 1
        elif mv > v:
            right = m - 1
    return -1

# def binaray_search_recursive(l,v):
#     left = 0
#     right = len(l) - 1
#     m = 0
#
#     m = (left + right) // 2
#     mv = l[m]
#     if mv == v:
#         return m
#     elif mv < v :
#         binaray_search_recursive(l[m+1:],v)
#     else:
#         binaray_search_recursive(l[:m - 1],v)
#     return -1
def binaray_search_recursive(l,v,left,right):
    if left > right:
        return -1
    m = (left + right) // 2
    mv = l[m]
    if m < 0 or m >= len(l):
        return -1
    if mv == v:
        return m
    if mv < v:
        left = m + 1
    elif mv > v:
        right = m - 1
    return binaray_search_recursive(l,v,left,right)


# print(binary_search([4,9,11,17,21,25,29,32,38],39))
print(binary_search([4,9,11,17,21,25,29,32,38],32))
# print(binary_search([4,9,11,17,21,25,29,32,38],9))
print(binaray_search_recursive([4,9,11,17,21,25,29,32,38],38,0,8))