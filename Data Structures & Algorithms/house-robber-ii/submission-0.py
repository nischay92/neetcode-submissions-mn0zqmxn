class Solution:
    def rob(self, nums: List[int]) -> int:
        return max( nums[0],self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, num):
        rob1 , rob2 = 0 , 0
        for n in num:
            newRob = max(rob1 + n , rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
    