class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}
        final = []
        
        for word in strs:
            frequencies = [0] * 26
            
            for letter in word:
                index = ord(letter) - ord('a')
                frequencies[index] += 1

            fixed = tuple(frequencies)

            if fixed in result:
                result[fixed].append(word)
            else:
                result[fixed] = [word]

        for key in result:
            final.append(result[key])

        return final

    
        

        