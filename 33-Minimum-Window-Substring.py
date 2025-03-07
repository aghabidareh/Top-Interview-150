class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target_count = {}
        for char in t:
            target_count[char] = target_count.get(char, 0) + 1

        window_count = {}
        left = 0
        right = 0
        min_len = float('inf')
        min_window = ""
        required = len(target_count)
        formed = 0
        while right < len(s):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
            while left <= right and formed == required:
                char = s[left]
                window_size = right - left + 1
                if window_size < min_len:
                    min_len = window_size
                    min_window = s[left:right + 1]
                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1
                left += 1
            right += 1
        return min_window