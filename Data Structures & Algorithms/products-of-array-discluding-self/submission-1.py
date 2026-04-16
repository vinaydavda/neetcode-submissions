class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            result.append(prod)
        return result

        # new_arr = []

        # for i in range(len(nums)):
        #     if i == 0:
        #         new_arr.append(math.prod(nums[i + 1:]))
        #     elif i == len(nums) - 1:
        #         new_arr.append(math.prod(nums[:i]))
        #     else:
        #         check_nums = nums[:i]
        #         check_nums.extend(nums[i + 1:])
        #         new_arr.append(math.prod(check_nums))

        # return new_arr