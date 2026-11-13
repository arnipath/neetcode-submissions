class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        i = 0
        #store sorted word and the index of the new list
        anagrams = {}
        for word in strs:
            sort = ''.join(sorted(word))
            if sort in anagrams:
                res[anagrams[sort]].append(word)
            else:
                res.append([word])
                anagrams[sort] = i
                i += 1
        return res
