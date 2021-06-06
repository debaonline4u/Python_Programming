
# coding: utf-8

#     My logic:
#     
#         1. First traverse the whole array from starting to find how many negative numbers are present.
#             If all numbers are negative, then starting from RHS of array, do square for all numbers.
#             If all numbers are positive, then starting from LHS of array, do square for all numbers. 
#         2. [If array has both positive and negative numbers]
#             Start 2 pointers[left,right], one pointer for positive numbers, one for negative numbers. 
#             Compare squares of the numbers pointed by left and right. 
#             Whichever square is lower, print that square and move the pointer accordingly. 
#             

#     Time complexity: O(n)
#     Space complexity: O(1)
#     Runtime: 228 ms [in leetcode]



class Solution:
    def sortedSquares(self, nums):
        sorted_squared_nums = []
        next_pointer = 0
        # Here I am getting howmany are -ve numbers
        for i in range(len(nums)):
            if nums[i] < 0:
                next_pointer += 1
        # Here I can also check, if all numbers are positive or all are negative, 
        # then just print the square start to last of nums array
        if next_pointer == 0: # i.e all positive numbers
            for x in nums:
                sorted_squared_nums.append(x*x)
            return sorted_squared_nums
        if next_pointer == len(nums): # i.e all negative numbers
            next_pointer -=1
            while next_pointer >= 0:
                sorted_squared_nums.append(nums[next_pointer] * nums[next_pointer])
                next_pointer -= 1
            return sorted_squared_nums
        
        # Here we can start 2 pointers, left and right
        left, right = next_pointer-1, next_pointer
        left_square, right_square = 0, 0
        while((left >= 0) and (right<len(nums))):
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if (left_square <= right_square):
                sorted_squared_nums.append(left_square)
                left -= 1
            else:
                sorted_squared_nums.append(right_square)
                right += 1
        
        # print those squares which are left
        if left >= 0:
            while(left>=0):
                sorted_squared_nums.append(nums[left] * nums[left])
                left -= 1
        if right < len(nums):
            while(right<len(nums)):
                sorted_squared_nums.append(nums[right] * nums[right])
                right += 1
        
        return sorted_squared_nums


# nums = [-4,-1,0,3,10]
# nums = [-4, -2, -1, 0]
nums = [-2, 0]


obj1 = Solution()
sorted_nums = obj1.sortedSquares(nums)
print(sorted_nums)

