"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Sol: Backtracking
"""

def letterCombination(digits):
    keyboard = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }

    if len(digits) == 0:
        return []
    
    def backtrack(combination, next_digit):
        if len(next_digit) == 0:
            res.append(combination)
        else:
            first_number = next_digit[0]
            for letter in keyboard[first_number]:
                backtrack(combination + letter, next_digit[1:])
    
    res = []
    backtrack("", digits)
    return res


digits = "234"
res = letterCombination(digits)
print(res)