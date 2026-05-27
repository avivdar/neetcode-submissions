class Solution(object):
    def removeDuplicates(self, nums):
        
        n = len(nums);
        if (n == 0):
            return 0


       

        insertIndex = 1
        for i in range(1,n):
            if(nums[i] != nums [i - 1]):
                nums[insertIndex] = nums[i]
                insertIndex += 1

        return insertIndex

       