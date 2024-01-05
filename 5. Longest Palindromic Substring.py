class Solution:
    def longestPalindrome(self, s: str) -> str:

        palindromic = ''

        for i in range(len(s)):
            if len(self.getlongestPalindromic(s, i, i)) > len(palindromic):
                palindromic = self.getlongestPalindromic(s, i, i)
            if len(self.getlongestPalindromic(s, i, i+1)) > len(palindromic):
                palindromic = self.getlongestPalindromic(s, i, i+1)
        return palindromic

    def getlongestPalindromic(self, s, l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


# 对撑按照中心对撑和轴对撑
# Input: s = "babad", Output: "bab"   是中心对撑。对一个letter他的左右letter是否相等，相等则继续l和r>>>>>>l-1 and r+1   同时 l>=0 and r< len(s)

# Input: s = "cbbd",Output: "bb" 是轴对称。letter -i = letter-i+1。相等则继续l和r>>>>>>l-1 and r+1   同时 l>=0 and r< len(s)
