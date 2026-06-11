class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        m, n = len(grid), len(grid[0])
        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))
        dist = 0 
        while queue:
            dist += 1 
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == 2147483647:
                            queue.append((nr, nc))
                            grid[nr][nc] = dist
        
