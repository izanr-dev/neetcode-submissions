from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        remaining = Counter(t)
        final = ""
        l = 0

        for r in range(len(s)):
            
            remaining[s[r]] -= 1

            while max(remaining.values()) <= 0:
                
                substring = s[l:r + 1]
                
                if final == "" or len(substring) < len(final):
                    final = substring

                remaining[s[l]] += 1
                l += 1

        return final