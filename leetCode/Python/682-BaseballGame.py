# 682. Baseball Game (Easy)
# https://leetcode.com/problems/baseball-game/
# Apply each operation to a score record (number = add, '+' = sum of last two,
# 'D' = double the last, 'C' = remove the last) and return the final sum.

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
