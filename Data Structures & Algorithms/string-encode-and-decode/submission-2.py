class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += word + "Ć"
        return string
    def decode(self, s: str) -> List[str]:
        strs = []
        currWord = ""
        for char in s:
            if char == 'Ć':
                strs.append(currWord)
                currWord = ""
            else:
                currWord += char
        return strs