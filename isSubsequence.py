#Returns true if s is a subsequence of t
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counts = {}
        for i in range(len(s)):
            if s[i] in t:
                index = t.index(s[i]) #this will return an error if not in so need conditional
            else:
                return False
            t = t[index+1:]
        return True
