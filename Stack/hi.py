digits = '23'
result = []
charDict = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}
def backtracking(index, curString):
    if len(curString) == len(digits):
        result.append(curString)
        return 
    for c in charDict[digits[index]]:
        backtracking(index + 1, curString + c)

if digits:
    backtracking(0, '')
print(result)
