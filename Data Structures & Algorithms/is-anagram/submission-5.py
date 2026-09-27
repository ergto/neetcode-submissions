class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sm={}
        tm={}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sm[s[i]] = 1 + sm.get(s[i], 0)
            tm[t[i]] = 1 + tm.get(t[i], 0)
        for i in sm:
            if sm[i] != tm.get(i, 0):
                return False
        return True
            
            
        