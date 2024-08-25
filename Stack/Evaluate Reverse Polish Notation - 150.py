class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+-*/':
                op1 = stack.pop()
                op2 = stack.pop()
                if i == '+':
                    stack.append(op1 + op2)
                elif i == '-':
                    stack.append(op2 - op1)
                elif i == '*':
                    stack.append(op1 * op2)
                else:
                    div = op2 / op1
                    if div < 0:
                        stack.append(math.ceil(div))
                    else:
                        stack.append(math.floor(div))
            else:
                stack.append(int(i))
        return stack[-1]
