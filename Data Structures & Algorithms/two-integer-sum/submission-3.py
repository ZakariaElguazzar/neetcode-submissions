class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exists = {}
        for i , value in enumerate(nums):
            complement = target - value
            if complement in exists:
                return [exists[complement], i]
            exists[value] = i
        return []
