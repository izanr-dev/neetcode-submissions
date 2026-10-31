class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        l = 0
        result = 0

        for r in (range(len(s))):

            new = s[r]
            while new in seen:
                seen.remove(s[l])
                l += 1

            seen.add(new)

            result = max(result, len(seen))
        
        return result


        """
        seen = []
        result = 0

        for letter in s:
            
            while letter in seen:
                seen.pop(0)
                
            seen.append(letter)
            result = max(result, len(seen))

        return result
        """