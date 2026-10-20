class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}
        
        for i, number in enumerate(numbers):

            diff = target - number

            if diff in seen:
                return[seen[diff]+1, i+1]

            seen[number] = i

        return []



