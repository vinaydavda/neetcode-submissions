class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        for l in range(len(s)):
            counts = {}
            max_f = 0

            for r in range(l, len(s)):
                # Increment current character count
                counts[s[r]] = 1 + counts.get(s[r], 0)

                window_size = r - l + 1
                max_f = max(max_f, counts[s[r]])

                if (window_size - max_f) <= k:
                    res = max(res, window_size)

        return res