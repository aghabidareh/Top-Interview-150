class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        the_number = 0
        count = len(digits) - 1

        for i in range(len(digits)):
            the_number+= digits[i]*(10**(count))
            count-=1

        the_number+=1
        l = str(the_number)
        arr = []

        for i in range(len(l)):
            arr.append(l[i])

        new_list = list(map(int, arr))

        return new_list