class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxList = []
        l = 0
        for r in range(k-1, len(nums)):
            temp = nums[l:r + 1]
            maxList.append(max(temp))
            l += 1
        return maxList