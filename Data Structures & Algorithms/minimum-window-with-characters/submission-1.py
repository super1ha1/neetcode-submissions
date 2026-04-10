class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        
        total = len(t)
        m = defaultdict(int)
        for c in t:
            m[c] += 1
        
        window = defaultdict(int)
        have = 0
        need = len(m)
        
        print(f'm {m} total {total}')
        # loop
        l = 0

        res = 0
        resLen = len(s) + 1

        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            print(f'loop for {r} {c}')

            if c in m and window[c] == m[c]:
                have += 1
            
            while have == need:               
                # now minimum, keep
                curLen = r  - l + 1
                print(f'res: {res} resLen {resLen} curLen: {curLen}')
                if curLen < resLen:
                    resLen = curLen
                    res = l

                window[s[l]] -= 1
                if s[l] in m and window[s[l]] < m[s[l]]:
                    have -= 1
                l += 1

        if resLen < len(s) + 1:
            return s[res: res + resLen]
        return ''



