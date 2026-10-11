class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}
        result = []

        for number in nums:
            if number in hashMap:
                hashMap[number] += 1
            else:
                hashMap[number] = 1

        for _ in range(k):
            
            max_freq = -1
            num = None
            
            for num, freq in hashMap.items():
                if freq > max_freq:
                    max_freq = freq
                    best_num = num

            result.append(best_num)
            del hashMap[best_num]

        return result
                    


                
        