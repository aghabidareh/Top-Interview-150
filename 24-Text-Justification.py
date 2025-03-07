class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, current, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(current) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    current[i%(len(current)-1 or 1)] += ' '
                result.append(''.join(current))
                current, num_of_letters = [], 0
            current += [w]
            num_of_letters += len(w)
        return result + [' '.join(current).ljust(maxWidth)]