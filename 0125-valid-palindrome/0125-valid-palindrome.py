class Solution:
    def isPalindrome(self, inp):
        s = [x.lower() for x in inp if x.isalnum()]
        return s == s[::-1]