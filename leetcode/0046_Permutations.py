"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 
Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    def permute(self, nums):
        ans = []
        def recursive(nums, track):
            if nums == []:
                ans.append(track[:])
                return
            
            for index in range(len(nums)):
                track.append(nums[index])
                new_nums = nums[:index] + nums[index+1:]
                recursive(new_nums, track)
                track.pop()
                
        recursive(nums, [])
        return ans



def main():
    nums = [1,2,3]

    solution = Solution()

    result = solution.permute(nums)
    
    print(result)


if __name__ == "__main__":
    main()