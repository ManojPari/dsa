# # from collections import Stack
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)

# print("Size of stack:", stack.size())
# print("Top item of stack:", stack.peek())

# while not stack.is_empty():
#     print("Popped item:", stack.pop())

# print("Size of stack:", stack.size())
def isValid(s: str):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False
    
    return not stack

s = "(){}}{"
print(isValid(s))