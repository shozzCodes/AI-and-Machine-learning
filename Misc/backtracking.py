class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res, sol = [], []
        def backt(i):
            if sum(sol) == target:
                res.append(sol.copy())
                return
            if i == len(candidates) or sum(sol) >= target:
                return
            sol.append(candidates[i])
            backt(i)
            sol.pop()
            backt(i+1)
        backt(0)
        return res
    def backtrack(self,index,arr:list):
        ans, sol = [], []
        def backt(i):
            if len(sol) == len(arr):
                ans.append(sol.copy())
                return
            if i >= len(arr):
                return 
            sol.append(arr[i])
            backt(i+1)
            sol.pop()
        backt(0)
        return ans
    def permute(self, nums: list[int]) -> list[list[int]]:
        res, sol = [], []
        visited = [False] * len(nums)
        def backt():
            if len(sol) == len(nums):
                res.append(sol.copy())
                return
            for i in range(len(nums)):
                
                if visited[i]:
                    continue

                sol.append(nums[i])
                visited[i] = True
                backt()
                sol.pop()
                visited[i] = False
        backt()
        return res
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        chck = []
        sol = ""
        def backt(p:str, n):
            nonlocal sol
            if len(sol) == 2*n and len(chck) == 0:
                res.append(sol)
                return
            if len(sol) >= 2*n:
                return
            for i in range(2*n):
                if p == "(":
                    chck.append(p)
                elif len(chck) != 0:
                    chck.pop()
                sol += p
                backt("(", n)
                sol = sol[:-1]
                backt(")", n)

        backt("(", n)
        return res            
    

nums = [1,2,3]
n = 2
sol = Solution()
print(sol.generateParenthesis(n))
# arr = ["shozab"]
# print(arr[0][1])
