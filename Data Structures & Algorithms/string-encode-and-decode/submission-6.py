class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs :
            return chr(256)

        encoded_str = ""
        
        for i in strs :
            encoded_str += i + chr(256)

        return encoded_str[:len(encoded_str)-1]

    def decode(self, s: str) -> List[str]:
        if s == chr(256) :
            return []
        return s.split(chr(256))        

