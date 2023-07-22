class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        odd = n//2
        even = n //2 + n%2
        return (self.recursive(5, even) % mod * self.recursive(4, odd) %mod) % mod


    def recursive(self, mult, n):
        mod = 10 **9 + 7
        if n == 0:
            return  1
        if n < 0:
            return 1/self.recursive(mult, -n)
        
        if n%2 == 0:
            return self.recursive((mult * mult)% mod, n //2)
        else:
            return mult * self.recursive((mult * mult)%mod, (n-1)//2)
