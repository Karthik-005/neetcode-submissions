class WordDictionary:

    def __init__(self):
        self.trie = {'eof':0}

    def addWord(self, word: str) -> None:
        curr = self.trie

        for i in word :
            if i not in curr :
                curr[i] = {'eof':0}
            curr = curr[i]

        curr['eof'] = 1        

    def search(self, word: str, curr=None) -> bool:
        print(word)
        if curr == None:
            curr = self.trie
        
        if not word:
            print(bool(curr['eof']))
            return bool(curr['eof'])

        for i in range(len(word)):
            print(curr)
            if word[i] == '.' and len(curr) > 1 :
                res = False
                for char in curr:
                    if char != 'eof'  and self.search(word[i+1:], curr[char]):
                        print(True)
                        res= True
                return res       
            
            elif word[i] in curr:
                curr=curr[word[i]]
            
            else :
                print(False)
                return False 
                
        print(bool(curr['eof']))
        return bool(curr['eof'])           




        
