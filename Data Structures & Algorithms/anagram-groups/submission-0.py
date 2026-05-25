class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hash map with:
        #keys = sorted strings
        #values = strs

        seenStrs = {}

        for i in range(len(strs)):
            strSorted = tuple(sorted(strs[i]))
            
            if strSorted in seenStrs:
                seenStrs[strSorted].append(strs[i])
            else:
                seenStrs[strSorted] = []
                seenStrs[strSorted].append(strs[i])
        
        return list(seenStrs.values())