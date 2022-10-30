def calculate(s):
    stack = []
    s += '+'
    pre_op = '+'
    num = 0
    i = 0
    while i < len(s):
        x = s[i]
        if x.isdigit():
            num = num * 10 + float(x)
        if x in '+-*/':
            if pre_op == '+':
                stack.append(num)
            if pre_op == '-':
                stack.append(-num)
            if pre_op == '*':
                stack[-1] *= num
            if pre_op == '/':
                tmp = stack.pop()
                stack.append(float(tmp/num))
            num = 0
            pre_op = x
        if x == '(':
            j = i
            # use cnt to keep track of the entire ()
            parenthesis = 0 
            while j < len(s):
                if s[j] == '(':
                    parenthesis += 1 
                if s[j] == ')':
                    parenthesis -= 1 
                if parenthesis == 0:
                    break
                j += 1
            num = calculate(s[i+1:j+1])
            i = j
        i += 1
    return sum(stack)
    
s = "(10+ 11)*(11/31)"
print (calculate(s))
