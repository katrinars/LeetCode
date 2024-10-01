class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []

        for char in s.lower():
            if char.isalnum():
                letters.append(char)

        return letters == letters[::-1]


        