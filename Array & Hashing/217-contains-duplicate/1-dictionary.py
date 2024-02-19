class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Fastest solution
        appeared = {}

        for num in nums:
            if num in appeared:
                return True
            else:
                appeared[num] = True
                
        return False
    
        # Time complexity: O(n) + O(1) = O(n)
        # Space complexity: O(n)