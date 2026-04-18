class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for w in range(len(words)): # row 
            for c in range(len(words[w])): # col 

                # If current word pos is > = the number of words
                # Or if number of words >= len of current word

                if c >= len(words) or \
                    w >= len(words[c]) or \
                    words[w][c] != words[c][w]:
                    return False
        return True
