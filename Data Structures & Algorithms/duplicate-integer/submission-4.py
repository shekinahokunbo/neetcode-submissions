class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

#iterate through each integer in the array
# check if the first number == second number, if not , keep moving till the end
# if at any pioin i = j, return true, else return false.
#try that first, then if it doesn't work, implement count
#length of the array is not always the same 


#new thought: create an empty set to store a number 
#iterate through the array
#keep the first number 

            # for num in nums:
            #     seen = []
            #     if num1 = num2
            #         if i == j:
            #             return True
            
            #     return False

        x = set(nums) 
        if len(nums) > len(list(x)):
            return True 
        return False

# set() - everything in this function is a key. so anytime you don't want more
# than one number, you use set. works in o[1] time. so you put the list they 
# #gave you, inside the set function. you can't order a set. you can't get first 
# number second number or third number. 
