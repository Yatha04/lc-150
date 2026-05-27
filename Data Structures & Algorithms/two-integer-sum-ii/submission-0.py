class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i in range (len(numbers)):
            rem = target - numbers[i]
            if (rem) in seen:
                if i < seen[rem]:
                    return [i+1, seen[rem]+1]
                else:
                    return [seen[rem] + 1, i + 1]
            seen[numbers[i]] = i
        