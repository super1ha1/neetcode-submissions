class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
            
        res = 0

        for i in range(len(s)):
            m = defaultdict(int)
            m[s[i]] = 1

            for j in range(i + 1, len(s)):
                m[s[j]] += 1
                # find top frequency
                top_frequency = max(m.values())
                cur = j - i + 1 
                if cur - top_frequency <= k:
                    res = max(res, cur)
        

        return res