from xml.sax import parse

from future.backports import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        https://leetcode.com/problems/valid-anagram/submissions/1672062573/
        :type s: str
        :type t: str
        :rtype: bool
                """
        # I. Hizli cozum
        # İki koleksiyonun (örneğin string, liste vs.) içerdiği elemanların sayılarıyla birlikte tamamen aynı olup olmadığını kontrol eder.
        #return Counter(s)==Counter(t) # hizli cozum

        # II. Hizli cozum
        # return sorted(s)==sorted(t)


        if not len(s) == len(t):
            return False
        s_sort =sorted(s)
        t_sort =sorted(t)
        return s_sort==t_sort


s = Solution()
print(s.isAnagram("rat", "cat"))
