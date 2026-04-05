from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        fmap = defaultdict(int)
        maxf = 0

        for r in range(len(s)):
            fmap[s[r]] += 1
            maxf = max(maxf, fmap[s[r]])

            # shrink window if too many replacements needed
            while (r - l + 1) - maxf > k:
                fmap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res