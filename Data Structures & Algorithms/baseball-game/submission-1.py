class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        stack = []

        for o in operations:
            if o == "+":
                total = stack[-1] + stack[-2]
                score += total
                stack.append(total)
            elif o == "D":
                double = 2 * stack[-1]
                score += double
                stack.append(double)
            elif o == "C":
                score -= stack.pop()
            else:
                score += int(o)
                stack.append(int(o))

        return score


        
        