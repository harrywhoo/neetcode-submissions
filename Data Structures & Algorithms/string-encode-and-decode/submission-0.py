class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for s in strs:
            length = len(s)
            encoded_str.append(str(length))
            encoded_str.append("%")
            encoded_str.append(s)
        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0 
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '%':
                j += 1 
            length = int(s[i:j])
            j += 1 
            decoded.append(s[j:j+length])
            i = j + length

        return decoded

