class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        for idx, num in enumerate(nums):
            for idxx, numm in enumerate(nums[idx + 1:]):
                if num == numm:
                    flag = True
                    break
        return flag