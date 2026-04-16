class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        checked = []
        for i in range(len(strs)):
            if i not in checked:
                checked.append(i)
                temp_result = [i]
                for j in range(i + 1, len(strs)):
                    if j not in checked:
                        if self.check_anagram(strs[i], strs[j]):
                            checked.append(j)
                            temp_result.append(j)
                temp_result = [strs[x] for x in temp_result]
                result.append(temp_result)
        return result

    def check_anagram(self, word1: str, word2: str) -> bool:
        check_dict = {}
        for i in word1:
            check_dict[i] = check_dict.get(i, 0) + 1
        
        for j in word2:
            check_dict[j] = check_dict.get(j, 0) - 1

        if all(c == 0 for c in check_dict.values()):
            return True
        else:
            return False
            
