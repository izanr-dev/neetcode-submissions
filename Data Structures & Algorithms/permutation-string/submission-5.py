from collections import Counter

def isPerm(s1: str, s2: str) -> bool:
        return(Counter(s1) == Counter(s2))

class Solution:
    
    def checkInclusion(self, s1: str, s2: str) -> bool:

        primary = len(s1)
        secondary = len(s2)

        if primary > secondary:
            return False

        for i, letter in enumerate(s2):
            
            tempstring = s2[i:i+primary]
            if isPerm(tempstring, s1):
                return True
        
        return False


