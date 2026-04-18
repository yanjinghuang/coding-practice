class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # words[i][j] == words[j][i] -> word square (symmetric)
        for w in range(len(words)): # row 
            for c in range(len(words[w])): # col 

                # If column index does not exist as a row
                # If row index does not exist in that column word

                if c >= len(words) or \
                    w >= len(words[c]) or \
                    words[w][c] != words[c][w]:
                    return False
        return True
