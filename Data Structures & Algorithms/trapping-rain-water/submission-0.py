class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * (len(height) + 1)
        suffix = [0] * (len(height) + 1)
        tot_vol = 0
        max_prefix = 0
        max_suffix = 0
        for i in range (len(height)):
            max_prefix = max(max_prefix, height[i])
            prefix[i + 1] = max_prefix

        for i in range(len(height)-1, -1,-1):
            max_suffix = max(max_suffix, height[i])
            suffix[i] = max_suffix
        print(prefix)
        print(suffix)

        for i in range(len(height)):
            vol = min(prefix[i + 1], suffix[i]) - height[i]
            tot_vol += vol
        
        return tot_vol

