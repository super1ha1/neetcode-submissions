class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = defaultdict(int)
        for i in s:
            m[i] += 1
        
        for i in t:
            m[i] -= 1
        
        for k, v in m.items():
            if v != 0:
                return False
        return True