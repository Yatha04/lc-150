class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #mix of prefix product and suffix product

        prefix = [0] * (len(nums) + 1)
        #[0,0,0,0,0]
        prefix[0] = 1
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] * nums[i]
        
        suffix = [0] * (len(nums) + 1)
        suffix[len(nums)] = 1
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = suffix[i+1] * nums[i]
        
        print(prefix)
        print(suffix)

        ans = [0] * len(nums)
        for i in range(len(ans)):
            ans[i] = suffix[i+1] * prefix[i]
        return ans