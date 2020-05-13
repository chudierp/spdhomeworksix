from typing import List

''' Leetcode #1: https://leetcode.com/problems/two-sum/ - Easy
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
            return [0, 1].
'''

''' Communication Steps
    1. Restate the problem
        I need to find two numbers that equal the target number when added together and return their index in the array.
    2. Ask clarifying questions
        Are there duplicates in this array? If so, would a duplicate be considered different elements since they'd have unique indices or should I remove duplicates first?
    3. State your assumptions
        I'm assuming each input has exactly one solution
        I'm assuming each element can only be used once
    4. Think out loud
        I can run through the array and find each number's corresponding partner by subtracting it from the target number.  I can use a queue to keep track of numbers I've already encountered.  If I subtract a number and I've already encountered its remainder, then those two are each other's complementary numbers, so I return their indices.  Since I need to return indices, my queue should be able to hold both numbers and their indices.  If I haven't encountered the remainder, then I add them to the queue.
'''

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        
        # go through nums list
        for index, current_num in enumerate(nums):
            # subtract current number from target to get remainder
            remainder = target - current_num

            # if remainder has already been encountered, return its index and the current number's index
            if remainder in checked:
                return [checked[remainder], index]
            
            # else, if current_num has not yet been encountered, 
            # add to checked dict with its index as value
            checked[current_num] = index

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    answer = Solution().two_sum(nums, target)
    print(f"Given the array: {nums}\n and the target: {target}")
    print(f"Indices of number in nums that add up to target: {answer}")