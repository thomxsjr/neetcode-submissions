class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            u = list(s)
            for v in t:
                if v in u:
                    u.remove(v)      
            if len(u) == 0:
                return True
        return False