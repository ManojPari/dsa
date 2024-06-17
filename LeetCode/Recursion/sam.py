# def evalRPN(tokens) -> int:
#     stack = []
#     for i in tokens:
#         if i == '+':
#             F = stack.pop()
#             S = stack.pop()
#             stack.append(int(S) + int(F))
#         elif i == '-':
#             F = stack.pop()
#             S = stack.pop()
#             stack.append(int(S) - int(F))
#         elif i == '*':
#             F = stack.pop()
#             S = stack.pop()
#             stack.append(int(S) * int(F))
#         elif i == '/':
#             F = stack.pop()
#             S = stack.pop()
#             stack.append(int(S/F))
#         else:
#             stack.append(int(i))      
#     return stack

# t = ["0","3","/"]
# print(evalRPN(t))

# def dailyTemperatures(temperatures):
#     ans = [0] * (len(temperatures))
#     stack = [0]
#     for i in range(1, len(temperatures)):
#         while stack and temperatures[i] > temperatures[stack[-1]]:
#             t = stack.pop()
#             ans[t] = i - t
#         stack.append(i)
#     return ans
# t = [73,74,75,71,69,72,76,73]
# print(dailyTemperatures(t))

def decodeString(s):
    stack = []
    current_num = 0
    current_str = ''

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char

    return current_str
string = "3[a2[c]]"
print(decodeString(string))
                
            