# The below solution is mine, and I think it is the best solution.
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        lookup = {}
        max_lookup = 0
        for word in strs: 
            word_dict = {}
            for letter in word: 
                if letter not in word_dict.keys(): 
                    word_dict[letter] = 1
                else: 
                    word_dict[letter] += 1
            found = 0
            for key, value in lookup.items(): 
                
                if word_dict == value: 
                    groups[key].append(word)
                    found = 1
                    break
            if found == 0: 
                max_lookup += 1
                lookup[max_lookup] = word_dict
                groups[max_lookup] = [word]
        
        return [value for value in groups.values()]