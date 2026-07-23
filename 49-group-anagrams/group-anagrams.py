class Solution(object):

    def sorting(self, s):
        s1 = list(s)
        s1.sort()
        return "".join(s1)

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dict1 = {}

        for i in strs:

            key = self.sorting(i)

            if key in dict1:

                dict1[key].append(i)
            else:

                dict1[key] = [i]

        return list(dict1.values())

        