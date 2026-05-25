class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #key: num, value: index
        rem = {}

        for i in range(len(nums)):
            check = target - nums[i]
            if check in rem:
                if i < rem[check]:
                    return [i,rem[check]]
                else:
                    return[rem[check], i]
            rem[nums[i]] = i
         