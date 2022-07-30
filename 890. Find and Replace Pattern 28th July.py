class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        matching = []
        hash_str = hash_word(pattern)
        for word in words:
            if hash_word(word) == hash_str:
                matching.append(word)

        return matching


def hash_word(word: str) -> list[int]:
    """Hash the given word into specific string"""
    letter_map = {}
    curr_map = 0
    map_list = []
    for letter in word:
        if letter not in letter_map.keys():
            curr_map += 1
            letter_map[letter] = curr_map
        map_list.append(letter_map[letter])
    return map_list
