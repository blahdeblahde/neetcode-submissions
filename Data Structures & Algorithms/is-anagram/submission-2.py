class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        deet = {}
        dees = {}
        if len(s) == len(t):
            for i in s:
                deet[i] = deet.get(i, 0) + 1
            for j in t:
                dees[j] = dees.get(j, 0) + 1
            return deet == dees
        else:
            return False

            