class Solution:
    def trap(self, height: List[int]) -> int:
        
        result = 0
        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]

        while l < r:
            if max_l < max_r:
                l+=1
                max_l = max(max_l, height[l])
                result += max_l - height[l]
            else:
                r-=1
                max_r = max(max_r, height[r])
                result += max_r - height[r]

        return result

        
        """
        result = 0

        for h in range(max(height)):
            
            row = [] 
            for i in range(len(height)):
                value = height[i] - h
                if value > 0: 
                    row.append(0)
                else:
                    row.append(1)
            l = 0
            r = len(height) - 1
            while (l<r):
                if row[l] == 0:
                    l+=1
                elif row[r] == 0:
                    r-=1
                else:
                    break
            if r - l > 0:
                while (l < r):
                    if row[l] == 0:
                        result+=1
                    l+=1

        return result
        """

        