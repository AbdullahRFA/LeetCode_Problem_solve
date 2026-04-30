'''
997. Find the Town Judge
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge. If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [a_i, b_i] representing that the person labeled a_i trusts the person labeled b_i. If the town judge exists and can be identified, return the label of the town judge. Otherwise, return -1.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2
Explanation: Person 1 trusts person 2, and person 2 trusts nobody. Thus, person 2 is the town judge.
Example 2:  
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Explanation: Both person 1 and person 2 trust person 3, and person 3 trusts nobody. Thus, person 3 is the town judge.
Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Explanation: Person 3 trusts person 1, so person 3 cannot be the town judge.
Example 4:
Input: n = 3, trust = [[1,2],[2,3]]
Output: -1

Intuition:
1. We can solve this problem by using two arrays to keep track of the number of people that trust each person and the number of people that each person trusts. We will iterate through the trust array and update these two arrays accordingly. After processing the trust array, we will check for each person if they are trusted by n-1 people and if they do not trust anyone. If we find such a person, we will return their label as the town judge. If we do not find such a person, we will return -1.

Approach:
1. We will initialize two arrays, ind and outd, of size n+1 to keep track of the number of people that trust each person and the number of people that each person trusts, respectively.
2. We will iterate through the trust array and for each pair [a_i, b_i], we will increment ind[b_i] by 1 and outd[a_i] by 1.
3. After processing the trust array, we will iterate through the range from 1 to n and check if there is a person i such that ind[i] is equal to n-1 and outd[i] is equal to 0. If we find such a person, we will return their label as the town judge.
4. If we do not find such a person after iterating through the range from 1 to n, we will return -1.

Time Complexity: O(n + m), where n is the number of people in the town and m is the length of the trust array. We will need to iterate through the trust array once to update the ind and outd arrays, which takes O(m) time. We will also need to iterate through the range from 1 to n to check for the town judge, which takes O(n) time. Therefore, the overall time complexity is O(n + m).

Space Complexity: O(n), where n is the number of people in the town. We will need to use two arrays of size n+1 to keep track of the number of people that trust each person and the number of people that each person trusts, which takes O(n) space. Therefore, the overall space complexity is O(n).


Another Solution:

Intuition:
1. We can also solve this problem by using a single array to keep track of the score of each person. We will iterate through the trust array and for each pair [a_i, b_i], we will decrement the score of a_i by 1 and increment the score of b_i by 1. After processing the trust array, we will check for each person if their score is equal to n-1. If we find such a person, we will return their label as the town judge. If we do not find such a person, we will return -1.

Approach:
1. We will initialize an array score of size n+1 to keep track of the score of each person.
2. We will iterate through the trust array and for each pair [a_i, b_i], we will decrement score[a_i] by 1 and increment score[b_i] by 1.
3. After processing the trust array, we will iterate through the range from 1 to n and check if there is a person i such that score[i] is equal to n-1. If we find such a person, we will return their label as the town judge.
4. If we do not find such a person after iterating through the range from 1 to n, we will return -1.

Time Complexity: O(n + m), where n is the number of people in the town and m is the length of the trust array. We will need to iterate through the trust array once to update the score array, which takes O(m) time. We will also need to iterate through the range from 1 to n to check for the town judge, which takes O(n) time. Therefore, the overall time complexity is O(n + m).

Space Complexity: O(n), where n is the number of people in the town. We will need to use an array of size n+1 to keep track of the score of each person, which takes O(n) space. Therefore, the overall space complexity is O(n). 
'''



from typing import List


# class Solution:
#     def findJudge(self, n: int, trust: List[List[int]]) -> int:
#         ind = [0]*(n+1)
#         outd = [0]*(n+1)

#         for people in trust:
#             ind[people[-1]]+=1
#             outd[people[0]]+=1
#         for i in range(1,n+1):
#             if ind[i]==n-1 and outd[i]==0:
#                 return i
#         return -1

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        score = [0]*(n+1)

        for people in trust:
            score[people[-1]]+=1
            score[people[0]]-=1
        for i in range(1,n+1):
            if score[i]==n-1:
                return i
        return -1