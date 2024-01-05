class Solution:
    def lengthOfLongestSubstring(s: str) -> int:

        start = -1
        max = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
                d[s[i]] = i
            else:
                d[s[i]] = i
                if i - start > max:
                    max = i-start
            print(d, max, start)
        print(max)


Solution.lengthOfLongestSubstring(s="abcabcbb")

sub = {}
cur_sub_start = 0
 cur_len = 0
  longest = 0

   for i, letter in enumerate(s):
        # in sub

        if letter in sub and sub[letter] >= cur_sub_start:
            cur_sub_start = sub[letter] + 1
            cur_len = i - sub[letter]
            sub[letter] = i

        # not in sub
        else:
            sub[letter] = i
            cur_len += 1
            if cur_len > longest:
                longest = cur_len

    return longest
