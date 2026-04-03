"""
🔹 Core Idea:
	•	Maintain a window [i → j]
	•	Keep product of elements in window
	•	Shrink window when condition breaks

⸻

⚙️ Step-by-Step Logic
	•	Expand window (j++)
	•	Multiply new element into product
	•	If product ≥ k → shrink window (i++)
	•	Count valid subarrays ending at j

⸻

"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k<1:
            return 0
        i=j=0
        ans = 0
        p = 1
        while(j<n):
            p*=nums[j]
            while i<=j and p>=k:
                p//=nums[i]
                i+=1
            ans += j-i+1
            j+=1
        return ans