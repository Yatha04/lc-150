class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        finalArr = []
        
        smallArr = []
        bigArr = []
        if len(nums1) > len(nums2):
            smallArr = nums2
            bigArr = nums1
        else:
            smallArr = nums1
            bigArr = nums2
        j = 0
        for i in range(len(smallArr)):
            while (j < len(bigArr) and bigArr[j] < smallArr[i]):
                finalArr.append(bigArr[j])
                j += 1
            finalArr.append(smallArr[i])
        while j < len(bigArr):
            finalArr.append(bigArr[j])
            j += 1

        print(finalArr)
        n = len(finalArr)
        if (n% 2 == 0):
            return (finalArr[n//2 - 1] + finalArr[n//2]) / 2
        else:
            return float(finalArr[n//2])