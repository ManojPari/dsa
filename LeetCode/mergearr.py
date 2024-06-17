
def mergeTwoSortedArraysWithoutExtraSpace(a, b) -> None:
    i = len(a) - 1
    j = len(b) - 1
    k = len(a) + len(b) - 1
    
    while j >= 0:
        if i >= 0 and a[i] > b[j]:
            a[k] = a[i]
            i -= 1
        else:
            a[k] = a[j]
            j -= 1
        k -= 1
        
# Example usage:

a = [1, 3, 5, 7, 9, 0, 0, 0, 0, 0]  # Make sure there is enough space for merging
b = [2, 4, 6, 8, 10]

mergeTwoSortedArraysWithoutExtraSpace(a, b)
print(a)