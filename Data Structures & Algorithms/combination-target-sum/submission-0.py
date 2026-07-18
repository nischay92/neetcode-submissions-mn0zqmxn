class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            # find the target
            if total == target:
                res.append(cur.copy())
                return
            # if target over shot
            if total > target or i >= len(nums):
                return
            # Decision Tree - case 1
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [] , 0)
        return res