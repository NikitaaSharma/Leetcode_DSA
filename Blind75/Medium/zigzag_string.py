"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
    string convert(string s, int numRows);
"""

def convert(s, numRows):
    if len(s) == 1 or numRows >= len(s):
        return s
    
    move = 1
    pattern = [[] for i in range(numRows)]
    index = 0
    for char in s:
        pattern[index].append(char)
        if index == 0:
            move = 1
        elif index == numRows - 1:
            move = - 1
        index += move

    for i in range(numRows):
        pattern[i] = ''.join(pattern[i])
    
    return ''.join(pattern)

s = "MICROSOFTISHIRING"
numRows = 3
res = convert(s, numRows)
print(res)