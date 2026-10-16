class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result =[]
        def solve(s,open_count,close_count):
            if len(s) == 2 * n:
                result.append(s)
                return 

            if open_count < n:
                solve(s + "(",open_count + 1, close_count)

            if close_count< open_count:
                solve(s + ")", open_count,close_count+1)

        solve("",0,0)
        return result
        