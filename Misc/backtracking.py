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
    def find_path(self, grid):
        direc = [
            (0,1),#right
            (0,-1),#left
            (1,0),#down
            (-1,0)#up
        ]
        visited_path = [[False] * len(grid[0]) for _ in range(len(grid))]
        res = []
        path = []
        def backt(dr,dc):
            path.append([dr, dc])
            visited_path[dr][dc] = True
            if grid[dr][dc] == 'E':
                res.append(path.copy())
                return
            for r, c in direc:
                
                row = dr + r
                col = dc + c
                if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                    continue
                if grid[row][col] == "#":
                    continue
                if visited_path[row][col]:
                    continue
                backt(row,col)
                visited_path[row][col] = False

            path.pop()

        backt(0,0)
        return res[0]
    
    def find(self, ch, grid):
        ans = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == ch:
                    ans.append([i,j])
        return ans

    def exist(self, board: list[list[str]], word: str) -> bool:
        pos = self.find(word[0], board)
        choices = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        string:list = []
        path = []
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i , j in enumerate(pos):
            #j[0] -> row and j[1] -> col
            def backt(dr,dc, index):
                if board[dr][dc] != word[index]:
                    return
                visited[dr][dc] = True
                path.append(board[dr][dc])
                if index == len(word) - 1:#base case
                    string.append(path.copy())
                    path.pop()
                    visited[dr][dc] = False
                    return
                for r , c in choices:
                    row = dr + r
                    col = dc + c
                    if not (0 <= row < len(board) and 0 <= col < len(board[0])):
                        continue
                    if board[row][col] != word[index+1]:
                        continue
                    if visited[row][col]:
                        continue
                    backt(row, col, index+1)

                path.pop()
                visited[dr][dc] = False
            backt(j[0], j[1], 0)

        
        temp = "".join(string[0]) if string else ""  
        if word == temp:
            return True

        return False

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        sol = []
        start = 0
        visited = [False] * len(candidates)
        def backt(i, start):
            if sum(sol) > target:
                start = True
                return
            if sum(sol) == target:
                res.append(sol.copy())

                return
            if i >= len(candidates):
                return
            for i in range(start , len(candidates)):
                if visited[i]:
                    continue
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                sol.append(candidates[i])
                visited[i] = True
                backt(i+1, i+1)
                visited[i] = False
                sol.pop()
            
        backt(0, start)
        return res
candidates = [9,2,2,4,6,1,5]
target = 8
sol = Solution()
print(sol.combinationSum2(candidates, target))
# # # arr = ["shozab"]
# ts = [[0, 2], [2, 1]]
# for i, j in enumerate(ts):
#     print(j[0], j[1])
# # print(arr[0][1])

