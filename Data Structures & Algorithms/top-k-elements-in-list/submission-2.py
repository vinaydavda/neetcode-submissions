class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = {}
        result = []

        # Got all counts - {num: occurrence}
        for num in nums:
            cnts[num] = 1 + cnts.get(num, 0)

        # Make a list
        cnts = [[j, i] for i, j in cnts.items()]

        # Sort list
        cnts.sort(reverse=True)

        # Get first K elements
        c = 0
        for cnt in cnts:
            c += 1
            result.append(cnt[-1])
            if c >= k:
                break

        return result

        # cnt = {}
        # result = []
        # for num in nums:
        #     if num not in cnt:
        #         cnt[num] = 0
        #     cnt[num] += 1

        # c = 0
        # sorted_cnt = dict(sorted(cnt.items(), key=lambda x: x[1], reverse=True))

        # for i in sorted_cnt.keys():
        #     result.append(i)
        #     c += 1
        #     if c >= k:
        #         break

        # return result