class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l < 3:
            return []
        nums.sort()
        numdict = {y:x for x, y in enumerate(nums)}
        result = []
        for i in range(l):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1,l):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                if -(nums[i] + nums[j]) in numdict:
                    if numdict[-(nums[i] + nums[j])] > j:
                        result.append([nums[i],nums[j],-(nums[i] + nums[j])])
        return result