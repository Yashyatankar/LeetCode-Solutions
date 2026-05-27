class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        first_word = strs[0]
        prefix = ""

        for i in range(len(first_word)):

            current_char = first_word[i]

            for word in strs:

                if i >= len(word) or word[i] != current_char:
                    return prefix

            prefix += current_char

        return prefix