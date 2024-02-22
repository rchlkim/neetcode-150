class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                curr = n + nums[left] + nums[right]

                if curr > 0:
                    right -= 1
                elif curr < 0:
                    left += 1
                else:
                    output.append([n, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return output
    
    # Time compleixty: O(nlogn) + O(n^2) = O(n^2)
    # Space coomplexity: O(1)