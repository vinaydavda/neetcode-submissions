class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [{i:j} for i, j in enumerate(nums)]
        for idx, num in enumerate(nums):
            for numm in nums[idx + 1:]:
                if list(num.values())[0] + list(numm.values())[0] == target:
                    return [list(num.keys())[0], list(numm.keys())[0]]