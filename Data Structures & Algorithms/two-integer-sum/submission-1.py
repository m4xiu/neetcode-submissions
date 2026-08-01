class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for i , n in enumerate (nums):
            dif = target - n
            if dif in prevmap:
                return [prevmap[dif],i]
            prevmap[n] = i
        return
        