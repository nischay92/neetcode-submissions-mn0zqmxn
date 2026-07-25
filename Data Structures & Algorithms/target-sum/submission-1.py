class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1 # for target 0, we can achieve it one way by not picking any of the nums

        for i in range(len(nums)):
            nextDp = defaultdict(int)
            for cur_sum, count in dp.items():
                nextDp[cur_sum + nums[i]] += count
                nextDp[cur_sum - nums[i]] += count
            dp = nextDp
        return dp[target]