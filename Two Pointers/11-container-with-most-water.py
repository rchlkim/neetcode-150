class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        most_water = 0
        l, r = 0, len(height) - 1

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = w * h
            
            if area > most_water:
                most_water = area
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return most_water

        
    # Time complexity: O(n)
    # Space complexity: O(1)