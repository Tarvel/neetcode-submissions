class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_w = ""
        for word in strs:
            encoded_w +=  "_encode_" + word
        return encoded_w

    def decode(self, s: str) -> List[str]:
        return s.split("_encode_")[1:]