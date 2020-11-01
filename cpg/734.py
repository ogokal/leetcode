class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """

    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here
        if len(words1) != len(words2):
            return False
        similiars = {}
        for pair in pairs:
            similiars[pair[0]] = pair[1]
            similiars[pair[1]] = pair[0]

        for w1, w2 in zip(words1, words2):
            if w1 != w2 and (w1 in similiars and w1 != similiars[w2]):
                print(w1 + " " + w2)
                return False
        return True
