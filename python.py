class Solution(object):

    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :return type: List:[int]
        '''

        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
    
# Example usage
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]