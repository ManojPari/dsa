def sort(index, s):
    if len(s) - 1 == index:
        return s
    for i in range(index, len(s)):
        if s[index] < s[i]:
            s[index], s[i] = s[i], s[index]
    return sort(index + 1, s)

s = [5, 4, 7, 9]
print(sort(0, s))