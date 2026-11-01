class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        result = 0
        frequencies = {}
        l = 0

        for r in range(len(s)):
            
            new = s[r]
            frequencies[new] = frequencies.get(new, 0) + 1

            while r - l + 1 - max(frequencies.values()) > k:
                old = s[l]
                frequencies[old] -= 1
                l += 1

            result = max(result, (r - l + 1))

        return result



        """
        seen = {}
        targetnum = 0

        for letter in s:
            if letter in seen:
                seen[letter] += 1
            else:
                seen[letter] = 1

        for letter in seen:
            targetnum = max(targetnum, seen[letter])

        l = len(s)
        print(targetnum)

        if k < l-targetnum:
            print('A')
            return targetnum + k
        else:
            print('B')
            return targetnum + (l - targetnum)
        """
            
        