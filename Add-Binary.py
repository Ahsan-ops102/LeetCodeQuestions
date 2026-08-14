class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i>=0 or j >=0 or carry:
            digit_a = int(a[i]) if i>=0 else 0
            digit_b = int(b[j]) if j>=0 else 0
            total = digit_a + digit_b + carry
            digit = total % 2
            new_carry = total // 2
            carry = new_carry
            result.insert(0, str(digit))
            i-=1
            j-=1

        return "".join(result)