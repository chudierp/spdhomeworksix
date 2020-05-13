from typing import List

''' Leetcode #15: https://leetcode.com/problems/3sum/ - Medium
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
    Example:
    Given array nums = [-1, 0, 1, 2, -1, -4],
    A solution set is:
        [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
'''

''' Communication Steps
    1. Restate the problem
        I need to find all the unique 3-number combinations within the given array that return zero when added together.
    2. Ask clarifying questions
        - Is it only the numerical values within the triplet that qualify a triplet as unique?  
        - Can a number be used in multiple triplets so long as the triplet itself has a unique set?
    3. State your assumptions
        - I'm assuming that a triplet can only use numbers with unique indices once.
        - Assuming array might contain no unique triplets that sum up to zero.
    4. Think out loud
        For each number in the array, I need to look for a pair of numbers that when added to it, equal to 0.  I can used three nested loops to do that but that seems pretty inefficient O(n^3).  I can't use what I did with two_sum because this array has duplicates.
        I can use the same strategy we saw in the google interview video, by sorting the array and then evaluating pairs, starting from the two ends of the array, with the smallest and largest numbers and moving towards the middle.
'''

class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        solutions = []

        nums.sort()

        for index, each in enumerate(nums):
            # This will run within leetcode time limit [part1] (https://leetcode.com/problems/3sum/discuss/183155/Two-pointer-python-solution-wexplanation-beats-91.75)
            if index > 0 and nums[index]==nums[index-1]:
                continue
            # Set starting index to next num in array, set last to last index in array
            start = index + 1
            end = len(nums) - 1

            # Run until pointers meet in the middle, no crossovers/overlap
            while start < end:
                sum_triplet = (each + nums[start] + nums[end])
                if sum_triplet == 0:
                    triplet = [each, nums[start], nums[end]]

                    # Avoid adding duplicate triplets  (too slow to pass leetcode)
                    # if triplet not in solutions:
                    #     solutions.append(triplet)

                    # This will run within leetcode time limit [part2] (https://leetcode.com/problems/3sum/discuss/183155/Two-pointer-python-solution-wexplanation-beats-91.75)
                    solutions.append(triplet)
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1

                    # Move both pointers up/down 1 respectively
                    start += 1
                    end -= 1
                # If sum is under target, move the starting pointer to the next(larger) value
                elif sum_triplet < 0:
                    start += 1
                # If the sum is over target, move the end pointer to the next (smaller) value
                else:
                    end -= 1

        if not solutions:
            return "No sets found"
        return solutions

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    answer = Solution().three_sum(nums)
    print(answer)