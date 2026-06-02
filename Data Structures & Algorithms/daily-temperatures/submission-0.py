class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):      # ← include last element
            days = 0
            found = False
            for j in range(i + 1, len(temperatures)):  # ← start at i+1, skip self-compare
                if temperatures[j] > temperatures[i]:
                    days = j - i               # ← cleaner than counting up
                    found = True
                    break
            result.append(days if found else 0) # ← always append something
        return result