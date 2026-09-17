class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueMap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in valueMap:
                return [valueMap[difference],i] 
            valueMap[nums[i]] = i

        