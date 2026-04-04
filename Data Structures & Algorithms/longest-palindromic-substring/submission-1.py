class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        n = len(s)
        start_index = 0
        resLen = 0
        
        for i in range(len(s)):
            # odd substring
            l = i
            r = i
            while l >= 0 and r < n and  s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    start_index = l

                l -= 1
                r += 1

            # even substring
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    start_index = l
                l -= 1
                r += 1

        return s[start_index: start_index + resLen]