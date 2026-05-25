class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = {}
        two = {}

        for i in s:
            one[i] = one.get(i,0) + 1
        for j in t:
            two[j] = two.get(j,0) + 1
        
        if one == two:
            return True
        else:
            return False