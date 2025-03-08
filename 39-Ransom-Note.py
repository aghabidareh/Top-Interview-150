class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = all(ransomNote.count(letter) <= magazine.count(letter) for letter in set(ransomNote))
        return result