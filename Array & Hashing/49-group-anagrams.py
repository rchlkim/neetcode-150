class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        collection = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s not in collection:
                collection[sorted_s] = []

            collection[sorted_s].append(s)

        return list(collection.values())
    
    # Time complexity: O(n) * O(mlogm) = O(n * mlogm)
    # Space complexity: O(n * m)