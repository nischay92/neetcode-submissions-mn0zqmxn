class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        large = 0
        while l < r:
            w = r - l
            h = min(heights[l],heights[r])
            area = w * h
            large = max(large,area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return large

