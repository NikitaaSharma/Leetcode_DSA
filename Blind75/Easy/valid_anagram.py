def isAnagram(s,t):
    if len(s) != len(t):
        return False
    
    prevMapS, prevMapT = {}, {}
    for i in range(len(s)):
        prevMapS[s[i]] = 1 + prevMapS.get(s[i], 0)
        prevMapT[t[i]] = 1 + prevMapT.get(t[i], 0)

    for x in prevMapS:
        if prevMapS[x] != prevMapT.get(x):
            return False
    return True

s = "anagram"
t = "nagaram"
res = isAnagram(s,t)
print(res)