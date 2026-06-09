class Solution:
  def dailyTemperatures(self, temperatures):
      result = [0] * len(temperatures)   # default 0 = "no warmer day" (our "-1" leftover case)
      stack = []                          # will hold INDICES, kept monotonic

      for i in range(len(temperatures)):  # i = current index, iterate ALL elements
            while stack and temperatures[i] > temperatures[stack[-1]]:
                poppedIndex = stack.pop()
                result[poppedIndex] = i - poppedIndex
            stack.append(i)
          
      return result