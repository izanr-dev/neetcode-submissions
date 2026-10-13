class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""

        for string in strs:
            
            encoded += str(f"{len(string):03d}")
            encoded += string

        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        
        result = []
        position = 0

        while (position < len(s)):
            
            length = int(s[position : position + 3])
            position += 3
            word = s[position : position + length]
            result.append(word)

            position += length

        return result
      
