class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust and N == 1:
            return 1
        h1, h2 = {}, {}
        for val in trust:
            h1[val[0]] = h1.get(val[0], 0) + 1
            h2[val[1]] = h2.get(val[1], 0) + 1
        for k, v in h2.items():
            if v == N - 1 and not h1.get(k):
                return k
        return -1
       
