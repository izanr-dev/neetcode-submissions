class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        length = len(nums)
        
        partialProductLeft = 1
        partialProductRight = 1
        leftProduct = []
        rightProduct = []

        counter = 0
        counterAlt = length -1

        while(counter < length):

            rightProduct.append(partialProductRight)
            partialProductRight *= nums[counter]

            leftProduct.append(partialProductLeft)
            partialProductLeft *= nums[counterAlt]

            counter += 1
            counterAlt -= 1
            
        for num in range(length):

            result.append(leftProduct[length - num - 1] * rightProduct[num])

        return result



        
        """
        result = []
        length = len(nums)
        partialProduct = 1
        
        for num in range(length):

            product = 1
            counter = num + 1
            
            while(counter < length):
                
                product *= nums[counter]
                counter += 1
                print(product)

            result.append(product*partialProduct)
            partialProduct *= nums[num]

        return result
        """
            
            


        