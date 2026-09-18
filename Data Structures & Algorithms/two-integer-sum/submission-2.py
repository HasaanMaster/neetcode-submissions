class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueMap = {}
        for i, num in enumerate(nums): 
            difference = target - num
            if difference in valueMap:
                return [valueMap[difference],i]
            valueMap[nums[i]] = i
        