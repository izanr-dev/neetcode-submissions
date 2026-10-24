class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res
        
        """
        seen = {}
        triplets = []
        orderedTriplets = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                total = nums[i] + nums[j]
                if total not in seen: 
                    seen[total] = []
                seen[total].append((i, j))

        for k in range(len(nums)):
            
            num = nums[k]
            target = -num

            if target in seen:
                for i, j in seen[target]:
                    if k != i and k != j:
                        temp = [num, nums[i], nums[j]]
                        tempS = temp.copy()
                        tempS.sort()

                        if tempS in orderedTriplets:
                            continue
                        triplets.append(temp)
                        orderedTriplets.append(tempS)
                
        return triplets
        """


        """
        triplets = []
        orderedTriplets = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):

                    if nums[i] + nums[j] + nums[k] == 0 and i != j and j != k and i != k:
                        
                        temp = [nums[i], nums[j], nums[k]]
                        tempS = temp.copy()
                        tempS.sort()

                        if tempS in orderedTriplets:
                            continue
                        triplets.append(temp)
                        orderedTriplets.append(tempS)

        return triplets
        """                