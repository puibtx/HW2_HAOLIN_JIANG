def calculate(s):
    return eval(s)
#def calculate(s):
#     stack = []
#     s += '+'
#     pre_op = '+'
#     num = 0
#     i = 0
#     while i < len(s):
#         X = s[i]
#         if X.isdigit():
#             num = num * 10 + int(X)
#         if X in '+-*/':
#             if pre_op == '+':
#                 stack.append(num)
#             if pre_op == '-':
#                 stack.append(-num)
#             if pre_op == '*':
#                 stack[-1] *= num
#             if pre_op == '/':
#                 tmp = stack.pop()
#                 stack.append(int(tmp/num))
#             num = 0
#             pre_op = X
#         if X == '(':
#             j = i
#             parent = 0 
#             while j < len(s):
#                 if s[j] == '(':
#                     parent += 1 
#                 if s[j] == ')':
#                     parent -= 1 
#                 if parent == 0:
#                     break
#                 j += 1
#             num = calculate(s[i+1:j+1])
#             i = j
#         i += 1
#     return sum(stack)
