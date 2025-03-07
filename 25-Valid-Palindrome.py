class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        translator = str.maketrans('', '', string.punctuation)
        s = s.translate(translator)
        s = s.replace(' ' , '')
        s = s.lower()

        is_palindrome = True
        for i in range(len(s)):
            if s[i] == s[-i-1]:
                is_palindrome = True
            else:
                is_palindrome = False
                break
        return is_palindrome