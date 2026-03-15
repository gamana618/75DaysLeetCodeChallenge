class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        array = set()
        output = []
        for num in nums:
            array.add(num)
        for i in range(1,n+1):
            if i  not in array:
                output.append(i)
        return output
        