class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #convert to ascii, then sort, then compare the two.
        sortedS = []
        sortedT = []

        for char in s:
            charValue = ord(char)
            sortedS.append(charValue)
        for char in t:
            charValue = ord(char)
            sortedT.append(charValue)

        if sorted(sortedS) == sorted(sortedT):
            return True
        else: return False