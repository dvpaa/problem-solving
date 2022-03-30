from itertools import combinations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x, y in combinations(list(range(len(nums))), 2):
            if nums[x] + nums[y] == target:
                return [x, y]