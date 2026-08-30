class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        hashmap = {}
        
        for i in nums1:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for num in nums2:
            if num in hashmap:


                if hashmap[num] != 0:
                    result.append(num)
                    hashmap[num] -= 1
        return result