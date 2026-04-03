class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        l = 0
        r = l + 1
        m = defaultdict(int)
        m[s[l]] = 1
        res = 1

        while l <= r and r < len(s):
            m[s[r]] += 1
            if m[s[r]] >= 2:
                while l <= r and m[s[r]] >= 2:
                    m[s[l]] -= 1
                    l += 1
                    
            else:
                # can append, compare result
                res = max(res, r - l + 1)
            print(l, r, m)
            
            r += 1
            
        

        return res


