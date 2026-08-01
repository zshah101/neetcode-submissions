class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "/", "*"}
        
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in operators:
                    result = 0
                    op = tokens[i]
                    a = int(tokens[i - 2]) 
                    b = int(tokens[i - 1])
                    if op == "+":
                        result = a + b
                    elif op == "-":
                        result = a - b
                    elif op == "*":
                        result = a * b
                    else:
                        result = int(a / b)

                    tokens[i-2] = str(result)
                    tokens.pop(i-1)
                    tokens.pop(i-1)
                    break

        return int(tokens[0])
            


                


        