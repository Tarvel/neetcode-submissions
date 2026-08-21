class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        
        for i, value in enumerate(nums):
            complement = target - value

            if complement in checked:
                return [checked[complement], i]
            
            checked[value] = i