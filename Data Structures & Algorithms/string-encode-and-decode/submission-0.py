class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''
        for i in strs:
            encodedStr += str(len(i))
            encodedStr += "#"
            encodedStr += i
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedStr = []
        i = 0
        while i < len(s):
            curr = ''
            readLen = ''
            while curr != '#' and i < len(s):
                curr = s[i]
                if curr != '#':
                    readLen += s[i]
                i += 1
            readLenInt = int(readLen)
            strAdd = ''
            for j in range(i,i+readLenInt):
                strAdd += s[j]
            decodedStr.append(strAdd)
            i += readLenInt
        return decodedStr


