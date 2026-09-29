class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for i in nums :
            if i not in occ:
                occ[i]=1
                continue
            occ[i]+=1
        occ = dict(sorted(occ.items(), key=lambda item: item[1], reverse=True))
        response = list(occ)[:k]
        return response
        