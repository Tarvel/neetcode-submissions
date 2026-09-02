class Solution:

    def encode(self, strs: List[str]) -> str:
        encrypted_words = {"encoded":""}
        for word in strs:
            text = "-"
            for letter in word:
                text = text + "#" + str(ord(letter))
            encrypted_words["encoded"] += text
        return encrypted_words["encoded"]

    def decode(self, s: str) -> List[str]:
        my_list = []
        for numbers in s.split("-")[1:]:
            text = ""
            for number in numbers.split("#")[1:]:
                number = int(number)
                text = text + chr(number)
            my_list.append(text)
        return my_list