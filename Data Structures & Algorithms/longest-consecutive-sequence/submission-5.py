class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Inspired from neetcode solution
        max_streak = 0
        nums = set(nums)  # For uniqueness

        for num in nums:
            streak = 0
            current = num

            while current in nums:
                streak += 1
                current += 1

            max_streak = max(streak, max_streak)
        
        return max_streak


        # My solution
        # # Remove duplicate
        # nums = set(nums)

        # # Ascending order - not needed as set automatically does this
        # nums = sorted(nums)

        # # Check for longest streak by checking in
        # # Where break start new
        # results = {}
        # max_len = 1 if nums else 0
        # max_len_key = None
        # for i in range(len(nums)):
        #     # Initialize with first as smallest consecutive list
        #     if i == 0:
        #         results[nums[i]] = [nums[i]]
        #         continue
            
        #     # If previous number matches - add current in it
        #     # print(results)
        #     prev_num = nums[i] - 1
        #     for idx, vals in results.items():
        #         if prev_num in vals:
        #             results[idx].append(nums[i])
        #             if len(results[idx]) > max_len:
        #                 max_len = len(results[idx])
        #                 max_len_key = idx
        #             break
            
        #     # If not a consecutive number - create a new list in results
        #     results[nums[i]] = [nums[i]]
            
        # return max_len
