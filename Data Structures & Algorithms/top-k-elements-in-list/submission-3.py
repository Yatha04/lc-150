class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        for key, value in freq.items():
            if value in count:
                count[value].append(key)
            else:
                count[value] = []
                count[value].append(key)
        sorted_nums = sorted(count.items(), reverse=True)
        ans = []
        for freq, numbers in sorted_nums:
            ans.extend(numbers)
            k -= len(numbers)
            if k == 0:
                return ans