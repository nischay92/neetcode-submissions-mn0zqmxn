class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in "+":
                stack.append(stack.pop() + stack.pop())
            elif c in "-":
                a , b = stack.pop() , stack.pop()
                stack.append(b - a)
            elif c in "*":
                stack.append(stack.pop() * stack.pop())
            elif c in "/":
                a , b = stack.pop() , stack.pop()
                stack.append(int(b / a))    
            else:
                stack.append(int(c))
        return stack[0]