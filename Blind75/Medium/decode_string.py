"""
link: https://leetcode.com/problems/decode-string/description/

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly
k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed,
etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for
those repeat numbers, k. For example, there will not be input like 3a or 2[4].

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
"""
def decodeString(s):
    stack = []
    curr_num = 0
    curr_str = ''

    for char in s:
        if char.isnumeric():
            curr_num = curr_num * 10 + int(char)
        elif char == '[':
            stack.append(curr_str)
            stack.append(curr_num)
            curr_num = 0
            curr_str = ''
        elif char == ']':
            count = stack.pop()
            prev_str = stack.pop()
            curr_str = prev_str + count * curr_str
        else:
            curr_str += char

    return curr_str

s = "3[a]2[bc]"
out = decodeString(s)
print(f'decoded string: {out}')