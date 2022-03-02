class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n+1):
            binary = '{0:b}'.format(i)
            ans.append(binary.count("1"))
        return ans

            
