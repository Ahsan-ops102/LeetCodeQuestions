class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set()

        for i in range(len(digits)):
            if digits[i] != 0:
                

                for j in range(len(digits)):
                    
                    for k in range(len(digits)):
                        if i != j and j != k and i != k:
                            if digits[k] % 2 == 0:
                                
                                result = digits[i] * 100 + digits[j] * 10 + digits[k]
                                numbers.add(result)
        return len(numbers)
