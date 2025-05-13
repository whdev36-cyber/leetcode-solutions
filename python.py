from collections import Counter

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
    
    def findEvenNumbers(self, digits):
        """
        :type digits List[int]
        :return type: List[int]
        """

        result = set()
        count = Counter(digits)

        for i in range(10):
            for j in range(10):
                for k in range(0, 10, 2):
                    tmp_count = Counter([i, j, k])

                    valid = True
                    for digit in tmp_count:
                        if tmp_count[digit] > count[digit]:
                            valid = False
                            break

                    if valid and i != 0:
                        num = 100 * i + 10 * j + k
                        result.add(num)

        return sorted(result)
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10
        
        return x == reversed_half or x == reversed_half // 10


    
# Example usage
solution = Solution()
# print(solution.findEvenNumbers([2,2,8,8,2]))
print(solution.isPalindrome(121))
print(solution.isPalindrome(122))