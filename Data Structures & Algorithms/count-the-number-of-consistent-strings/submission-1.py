class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = len(words)

        for w in words:
            for ch in w:
                if ch not in allowed:
                    res -= 1
                    break
        
        return res 

                    



        