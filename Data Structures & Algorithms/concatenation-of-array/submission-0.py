class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums  
        return ans  

print(Solution().getConcatenation([1,2,3,4,5]))