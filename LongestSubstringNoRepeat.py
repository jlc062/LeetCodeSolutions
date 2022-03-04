#Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        hashmap = {}

        res = 0
        while right < len(s):
            char = s[right]

            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
            while hashmap[char] > 1:
                char_l = s[left]
                if char_l not in hashmap:
                    hashmap[char_l] =1
                else:
                    hashmap[char_l] -=1
                left += 1
            res = max(res, right- left + 1)
            right += 1
        return res
