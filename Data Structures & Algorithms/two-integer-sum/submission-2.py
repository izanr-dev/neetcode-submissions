class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        #Inefficient
        """
            length = len(nums)

            for i in range(length):
                for j in range(length):
                    if (nums[i] + nums[j] == target) and (i != j):
                        return ([i, j])

            return "Error"
        """

        #Works but is too complicated
        """
        length = len(nums)
        map = {}

        for i in range(length):
            keyValue = target - nums[i]
            if nums[i] in map:
                return ([map[nums[i]], i])
            map[keyValue] = i

        return [-1] 
        """

        #Intuitive and efficient
        length = len(nums)
        seen = {}

        for i in range(length):
            needed = target - nums[i]
            if needed in seen:
                return([seen[needed], i])
            seen[nums[i]] = i

        return [] 



