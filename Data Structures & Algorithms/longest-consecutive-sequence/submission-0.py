class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        seq = 0
        max_seq = 0
        for i in numSet:
            print(i)
            if (i - 1) not in numSet:
                seq = 0
                j = i
                while j in numSet:
                    seq +=1
                    j += 1
                max_seq = max(seq, max_seq)
        return max_seq

