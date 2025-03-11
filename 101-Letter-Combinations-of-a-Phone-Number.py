class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(curr_str, current_digit):
            if len(current_digit) == 0:
                result.append(curr_str)
            else:
                for letter in numbers_to_letters[current_digit[0]]:
                    backtrack(curr_str + letter, current_digit[1:])

        if not digits:
            return []

        numbers_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []
        backtrack("", digits)
        return result