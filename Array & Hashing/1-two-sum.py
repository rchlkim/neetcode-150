class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        appeared = {}

        for i in range(len(nums)):
            if target - nums[i] in appeared:
                return appeared[target - nums[i]], i
            else:
                appeared[nums[i]] = i
        
        return [-1 -1]
                
        # Time complexity: O(n) + O(1) = O(n)
        # Space complexity: O(n)