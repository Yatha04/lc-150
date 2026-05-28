class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        freqS1 = {}
        freqS2 = {}

        for i in s1:
            freqS1[i] = freqS1.get(i,0) + 1
        print(freqS1)
        for right in range(len(s2)):

            if (right - left + 1) > len(s1):
                freqS2[s2[left]] = freqS2.get(s2[left], 0) - 1
                if freqS2[s2[left]] == 0:
                    del freqS2[s2[left]]
                left += 1
                
            freqS2[s2[right]] = freqS2.get(s2[right],0) + 1
            print(freqS2)
            if freqS1 == freqS2:
                return True
        return False