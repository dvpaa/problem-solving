class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for word in strs:
            w = ''.join(sorted(word))
            anagrams.setdefault(w, [])
            anagrams[w].append(word)
        return list(anagrams.values())