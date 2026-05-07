'''

'''


class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1
        count = 9
        start = 1

        while n> count*digit_length:
            n-=count*digit_length
            count*=10
            start*=10
            digit_length +=1
        
        number = start+(n-1)//digit_length
        idx = (n-1)%digit_length

        return int(str(number)[idx])