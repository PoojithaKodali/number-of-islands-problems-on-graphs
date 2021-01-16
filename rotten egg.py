class Solution:
    def orangesRotting(self, g: 'List[List[int]]') -> 'int':
        q, good = [], 0
        for i, r in enumerate(g):
            for j, c in enumerate(r):
                if c == 2: q.append((i, j))
                elif c == 1: good += 1
        total, m, n = 0, len(g), len(g[0])                       
        while q:
            nxt_q = []
            if good == 0: return total
            total += 1
            for i, j in q:
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < m and 0 <= y < n and g[x][y] == 1:
                        g[x][y] = 2
                        good -= 1                        
                        nxt_q.append((x, y))
            q = nxt_q
        return total if good == 0 else -1
	
	
