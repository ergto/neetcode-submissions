class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        save ={}
    
        save_2 ={}
        
        

        if len(s)!=len(t):
            return False

        #creating both hashmaps         
        for i in range(len(s)):
            save[s[i]] = 1 + save.get(s[i], 0)
            save_2[t[i]] = 1 + save_2.get(t[i], 0)

        for c in save:
            if save[c] != save_2.get(c,0):
                return False
        return True
        
            
            
        