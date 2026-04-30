class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for i in strs:
            encodedString += i+"±"
        return encodedString
    def decode(self, s: str) -> List[str]:
        currWord = ""
        decodedList = []
        for i in s:
            if i != "±":
                currWord += i
            else: 
                decodedList.append(currWord)
                currWord = ""
        return decodedList

