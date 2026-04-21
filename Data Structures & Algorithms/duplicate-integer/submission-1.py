class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): 
                if nums[i] == nums[j]:
                    return True
        return False




            
        


# UMPIRE METHOD: Iterate through the array,
# Pick a number from the array. check if that number's count is more than 1
# if it is, then true,
# if it is not, then go to the next number 

        