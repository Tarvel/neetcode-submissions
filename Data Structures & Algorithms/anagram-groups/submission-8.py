class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}
        
        for word in strs:
            # 1. Sort the word to find its "folder" name
            sorted_word = "".join(sorted(word))
            
            # 2. If the folder doesn't exist, create it. Then append the word.
            anagram_map.setdefault(sorted_word, []).append(word)
            
        # 3. Return all the folders
        return list(anagram_map.values())