class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_character = {}
        left = 0
        result = 0
        for right in range(len(s)):
            if s[right] not in seen_character:
                result = max(result,right-left+1)
            else:
                if seen_character[s[right]] < left:
                    result = max(result,right-left+1)
                else:
                    left = seen_character[s[right]] + 1
            seen_character[s[right]] = right
        return result