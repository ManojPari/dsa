result, sol = [], []
nums = [1,2,3]
def backtracking():
    if len(sol) == len(nums):
        result.append(sol[:])
        return
    
    for i in nums:
        if i not in sol:
            sol.append(i)
            backtracking()
            sol.pop()
backtracking()
print(result)