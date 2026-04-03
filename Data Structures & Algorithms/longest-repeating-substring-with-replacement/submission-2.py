class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)

        res = 0
        m = defaultdict(int)
        l = 0
        maxf = 0
        for r in range(len(s)):
            m[s[r]] += 1
            maxf = max(maxf, m[s[r]])

            len_cur = r - l + 1
            if len_cur - maxf <= k:
                res = max(res, len_cur)
            else:
                # shrink left
                m[s[l]] -= 1
                l += 1

        
        return res