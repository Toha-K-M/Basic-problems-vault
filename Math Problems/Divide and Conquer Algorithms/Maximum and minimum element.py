def find_max(li, left, right):
    if left == right:
        return li[left]
    mid = int((left + right) / 2)
    max1 = find_max(li, left, mid)
    max2 = find_max(li, mid + 1, right)
    return max1 if max1 > max2 else max2



li = [1, 5, 2, 9, 30, 7, 5, 2, 10]
print("Maximum element of the list is", find_max(li, 0, len(li) - 1))

# z = [40,30]
# print("min: ",find_max(z,0,len(z)-1) )
