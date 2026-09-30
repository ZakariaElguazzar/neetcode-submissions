class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exists = {}
        for index , value in enumerate(nums):
            complement = target - value
            if complement in exists and exists[complement] != index :
                return [exists[complement], index]
            exists[value] = index
        return []
