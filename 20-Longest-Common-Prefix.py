class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''

        strings = sorted(strs)
        first_string = strings[0]
        last_string = strings[-1]
        for i in range(min(len(first_string), len(last_string))):
            if first_string[i] != last_string[i]:
                return answer
            answer += first_string[i]

        return answer