class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for cur in strs:
            count = [0] * 26
            for c in cur:
                count[ord(c) - ord('a')] += 1
            print(tuple(count))
            m[tuple(count)].append(cur)

        return list(m.values())
        