class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for cur in strs:
            new_cur = ''.join(sorted(cur))
            print(cur, new_cur)
            if new_cur in m:
                m[new_cur].append(cur)
            else:
                m[new_cur] = [cur]
        
        return list(m.values())
        