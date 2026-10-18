class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        treatedNums = sorted(set(nums))

        longestYet = 1
        actualSeq = 1

        for i in range(1, len(treatedNums)):
        
            if treatedNums[i] == treatedNums[i-1] + 1:
                actualSeq += 1
                if actualSeq > longestYet:
                    longestYet = actualSeq
            
            else:
                actualSeq = 1

        return longestYet
        

        
        