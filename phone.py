from typing import List


class Solution:
    dict = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def combination(self, digits: str) -> List[str]:
        if not digits:
            return []
        if len(digits) == 1:
            return self.dict[digits]
        res1 = self.combination(digits[0])
        res2 = self.combination(digits[1:])
        return [a+b for a in res1 for b in res2]