'''
2225. Find Players With Zero or One Losses
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match. Return a list answer of size 2 where:
answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Example 1:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation: Players 1, 2, and 10 have not lost any matches.
 Players 4, 5, 7, and 8 each have lost one match.
 Players 3, 6, and 9 each have lost two matches.
Example 2:
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation: Players 1, 2, 5, and 6 have not lost any matches.
 Players 3 and 4 each have lost two matches.
Example 3:
Input: matches = [[1,2],[2,3],[3,4],[4,5]]
Output: [[1], [2, 3, 4]]
Explanation: Player 1 has not lost any matches.
 Players 2, 3, and 4 each have lost one match.
 
Constraints:
1 <= matches.length <= 10^5
matches[i].length == 2
1 <= winneri, loseri <= 10^5
winneri != loseri
All matches[i] are distinct.

Intuition:
1. We can solve this problem by using a dictionary to keep track of the number of losses for each player. We will iterate through the matches array and update the dictionary accordingly. After we have processed all the matches, we will iterate through the dictionary and separate the players into two lists: one for players with zero losses and another for players with exactly one loss. Finally, we will sort both lists and return them as the final answer.   

Approach:
1. We will initialize an empty dictionary called win_loss to keep track of the number of losses for each player. We will also initialize two empty lists, zero_losses and one_losses, to store the players with zero losses and one loss, respectively.
2. We will iterate through the matches array and for each match, we will update the win_loss dictionary. We will increment the loss count for the losing player and ensure that the winning player is also present in the dictionary with a loss count of zero if they have not been encountered before.
3. After processing all the matches, we will iterate through the win_loss dictionary and check the loss count for each player. If a player has zero losses, we will add them to the zero_losses list. If a player has exactly one loss, we will add them to the one_losses list.
4. Finally, we will sort both the zero_losses and one_losses lists in increasing order and return them as the final answer. 

Time Complexity: O(N log N), where N is the number of matches. We will need to iterate through the matches array once to build the win_loss dictionary, which takes O(N) time. Then, we will need to iterate through the win_loss dictionary to separate the players into two lists, which takes O(M) time, where M is the number of unique players. Finally, we will need to sort both lists, which takes O(K log K) time for each list, where K is the number of players in each list. In the worst case, if all players are unique and have either zero or one loss, this could take O(N log N) time.

Space ComplexityO(M), where M is the number of unique players. We will need to use a dictionary to keep track of the losses for each player, which takes O(M) space.: 


'''


from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_loss = {}
        zero_losses = []
        one_losses = []

        for w, l in matches:
            win_loss[w] = win_loss.get(w, 0)+0
            win_loss[l] = win_loss.get(l, 0)+1

        for k,v in win_loss.items():
            if v == 0:
                zero_losses.append(k)
            elif v == 1:
                one_losses.append(k)
        zero_losses.sort()
        one_losses.sort()
        return [zero_losses, one_losses]