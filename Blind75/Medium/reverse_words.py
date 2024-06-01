"""
link:  https://leetcode.com/problems/reverse-words-in-a-string/\


"""

def reverseWords(s):
    res, i, n = '', 0, len(s)
    while i < n:
        while i < n and s[i] == ' ':
            i +=1
        j = i+1
        while j < n and s[j] != ' ':
            j +=1
        word = s[i:j]
        if len(res) == 0: res = word
        else:
            res = (word + " " + res).strip(" ")
        i = j+ 1
    return res


s = "sphinx of black quartz judge my vow"
out = reverseWords(s)
print(f'-{out}-')