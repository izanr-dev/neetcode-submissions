class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        revisados = set()

        for n in nums:
            if(n in revisados):
                return True
            else:
                revisados.add(n)

        return False
        