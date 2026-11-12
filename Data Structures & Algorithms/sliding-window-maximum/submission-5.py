from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        sw = deque()  
        result = []

        for i, num in enumerate(nums):
            if sw and sw[0] <= i - k:
                sw.popleft()

            while sw and nums[sw[-1]] < num:
                sw.pop()

            sw.append(i)

            if i >= k - 1:
                result.append(nums[sw[0]])

        return result

        """
        sw = deque(nums[0:k])
        counter = k
        result = []
        
        while counter < len(nums):

            result.append(max(sw))
            sw.popleft()
            sw.append(nums[counter])
            counter+=1

        result.append(max(sw))
        return result
        """
        