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
    
    def threeConsecutiveOdds(self, arr):
        '''
        :type arr: List[int]
        return type: bool
        '''
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        return False
            
    
# Example usage
solution = Solution()
print(solution.threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12]))