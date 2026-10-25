class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j = len(heights) - 1

        best = 0

        while (j > i):

            volume = (j - i) * (min(heights[i], heights[j]))
            best = max(volume, best)
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1

        return best


        """
        best = 0
        for i in range(len(heights)):
            for j in range(len(heights)):

                x = i - j
                if 0 > x:
                    x = -x

                y = min(heights[i], heights[j])
                
                volume = x * y

                if volume > best:
                    best = volume

        return best
        """