class Solution:

    
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        

        def meter(c):
                if c in first:
                    first[c] += 1
                else:
                    first[c] = 1
        
        def sacar(c):
            if (c in first and first[c] > 1):
                first[c] -= 1
            elif (c in first and first[c] == 1):
                del first[c]
            else:
                return False
        
        
        first = {}

        for letter in s:
            meter(letter)

        for letter in t:
            sacar(letter)
        
        if len(first) > 0:
            return False

        return True

        
                 