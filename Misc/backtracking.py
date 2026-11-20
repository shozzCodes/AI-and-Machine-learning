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
candidates = [1,2]
target = 4
sol = Solution()
print(sol.combinationSum(candidates, target))
