class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def actual(s):
            st = []
            for ss in s:
                if ss == "#":
                    if len(st) > 0:
                        st.pop()
                else:
                    st.append(ss)
            return "".join(st)
        ss = actual(S)
        tt = actual(T)
        return ss == tt
