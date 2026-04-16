class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        result = []
        for num in nums:
            if num not in cnt:
                cnt[num] = 0
            cnt[num] += 1

        # cnt = {j:i for i, j in cnt.items()}
        print(cnt)

        c = 0
        sorted_cnt = dict(sorted(cnt.items(), key=lambda x: x[1], reverse=True))
        print(sorted_cnt)
        for i in sorted_cnt.keys():
            result.append(i)
            c += 1
            if c >= k:
                break

        return result