class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(leftp, rightp):
            if leftp == rightp == n:
                res.append("".join(stack))

            if leftp < n:
                stack.append("(")
                backtrack(leftp + 1, rightp)
                stack.pop()

            if rightp < leftp:
                stack.append(")")
                backtrack(leftp, rightp + 1)
                stack.pop()

        backtrack(0, 0)
        return res