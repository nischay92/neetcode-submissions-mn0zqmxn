class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]: 
                return m
            # if nums[l] <= nums[m]:
            #     if target > nums[m] or target < nums[l]:
            #         l = m + 1
            #     else:
            #         r = m - 1
            # else:
            #     if target < nums[m] or target > nums[r]:
            #         r = m - 1
            #     else :
            #         l = m + 1
            if nums[l] <= nums[m]:
                #target inside left sorted array
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
                
                
