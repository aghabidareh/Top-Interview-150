class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                number2 = stack.pop()
                number1 = stack.pop()
                if token == "+":
                    stack.append(number1 + number2)
                elif token == "-":
                    stack.append(number1 - number2)
                elif token == "*":
                    stack.append(number1 * number2)
                elif token == "/":
                    stack.append(int(float(number1) / number2))
        return stack.pop()