class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ts = ""

        for letter in s:
            if letter.isalnum():
                ts+=letter.lower()

        if not ts:
            return True
        length = len(ts)

        i = 0
        while (i <= length//2):
            print(ts[i], ts[length - 1 - i])
            if ts[i] != ts[length - 1 - i]:
                return False
            i+=1

        return True