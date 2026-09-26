class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        preMap = {}

        for i,n in enumerate(nums):
            if n in preMap:
                return True
            
            preMap[n] = i
        return False
        