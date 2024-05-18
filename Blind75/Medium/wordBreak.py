"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Example: Input: s = "leetcode", wordDict = ["leet", "code"], Output: true

Sol: DP
"""

def wordBreak(s, wordDict):
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True

    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    
    return dp[-1]

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
res = wordBreak(s, wordDict)
print(res)