class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dic1 = self.check_dict(s[i], dic1)
            dic2 = self.check_dict(t[i], dic2)
        return dic1 == dic2
    
    def check_dict(self, num: int, dic: dict):
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
        return dic 
        