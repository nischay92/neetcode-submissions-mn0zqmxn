class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        # length is the number of original balloons in the interval.
        for length in range(1, n - 1):
            for left in range(1, n - length):
                right = left + length - 1

                for last in range(left, right + 1):
                    coins = (
                        nums[left - 1] * nums[last] * nums[right + 1]
                        + dp[left][last - 1]
                        + dp[last + 1][right]
                    )

                    dp[left][right] = max(dp[left][right], coins)

        return dp[1][n - 2]