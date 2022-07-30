class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return form_letter_dict(s) == form_letter_dict(t)


def form_letter_dict(word) -> dict[str, int]:
    frequency_dict = {}
    for letter in word:
        if letter not in frequency_dict:
            frequency_dict[letter] = 1
        else:
            frequency_dict[letter] += 1
    return frequency_dict
