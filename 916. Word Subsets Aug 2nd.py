def wordSubsets(words1, words2):
    lst = []
    for word1 in words1:
        letter_dict = formLetterDict(word1)
        for word2 in words2:
            # breakpoint()
            flag = 0
            ltr = letter_dict.copy()
            for letter in word2:
                if letter not in ltr.keys() or ltr[letter] < 1:
                    flag = -1
                    break
                else:
                    ltr[letter] -= 1
            if flag == 0:
                lst.append(word1)



    return lst
    # for key, value in count.items():
    #     if value == len(words2):
    #         lst.append(key)
    # return lst


def formLetterDict(word: str) -> dict[str, int]:
    ltr_dict = {}
    for i in word:
        if i in ltr_dict.keys():
            ltr_dict[i] += 1
        else:
            ltr_dict[i] = 1
    return ltr_dict
