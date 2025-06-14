"""
You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:

When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.


Example 1:

Input: num = 11891
Output: 99009
Explanation:
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.
Example 2:

Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.


Constraints:

1 <= num <= 108
"""
"""
🔍 Step-by-Step Explanation
	1.	Convert the number to a string to work with its digits.
	2.	For maximum value:
	    •	Replace the first non-9 digit with 9 using str.replace().
	    •	This maximizes the number by changing the smallest impactful digit.
	3.	For minimum value:
	    •	Replace the first non-0 digit with 0 using str.replace().
	    •	This minimizes the number by reducing the largest impactful digit.
	4.	Return the difference between max and min.
"""
class Solution:
    def minMaxDifference(self, num: int) -> int:
        # temp = str(num)
        # num_list = [x for x in temp]
        # # print(num_list)
        # fg = '-1'
        # for i in range(len(num_list)):
        #     if int(num_list[i]) != 9:
        #         fg = num_list[i]
        #         num_list[i] = '9'
        #         break
        # # print(type(fg))
        # for i in range(len(num_list)):
        #     if num_list[i] == fg:
        #         num_list[i] = '9'
        # str_max_num = ''
        # for x in num_list:
        #     str_max_num+=x
        # str_max_num = int(str_max_num)
        # # print(str_max_num)
        #
        # tempp = str(num)
        # numb_list = [x for x in tempp]
        # # print(numb_list)
        # fgg = '-1'
        # for i in range(len(numb_list)):
        #     if int(numb_list[i]) != 0:
        #         fgg = numb_list[i]
        #         numb_list[i] = '0'
        #         break
        # # print(type(fg))
        # for i in range(len(numb_list)):
        #     if numb_list[i] == fgg:
        #         numb_list[i] = '0'
        # str_min_num = ''
        # for x in numb_list:
        #     str_min_num+=x
        # str_min_num = int(str_min_num)
        # # print(str_min_num)
        # return str_max_num-str_min_num
        temp = str(num)
        for x in temp:
            if x != '9':
                max_value = int(temp.replace(x,'9'))
                break
        else:
            max_value = num
        for x in temp:
            if x != '0':
                min_value = int(temp.replace(x,'0'))
                break
        else:
            min_value = num
        return max_value - min_value

slv = Solution()
num = 90
print(slv.minMaxDifference(num))