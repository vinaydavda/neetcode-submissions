class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "##"
        return "&&".join(strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "##":
            return []
        if s == "":
            return [""]
        return s.split("&&")
