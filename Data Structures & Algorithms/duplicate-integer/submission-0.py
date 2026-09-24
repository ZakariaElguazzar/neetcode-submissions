class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Seen = {}
        for i in nums :
            if i not in Seen:
                Seen[i]=1
            else:
                return True
        return False