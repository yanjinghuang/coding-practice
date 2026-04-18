class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res 

    #5#hello5#world
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i # Use j to track the pos of #
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            letter = s[j+1: j+1+length]
            res.append(letter)
            i = j+1+length 
        return res


