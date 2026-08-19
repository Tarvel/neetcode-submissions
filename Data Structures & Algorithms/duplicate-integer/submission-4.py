class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = []
        for i in range(len(nums)):
            if nums[i] in test:
                det = "in"
                test.append(nums[i])
                test.append(det)
            else:
                test.append(nums[i])
                
        if "in" in test:
            final = True
        else:
            final = False
        
        return final
        