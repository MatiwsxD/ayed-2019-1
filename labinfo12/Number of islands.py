def numIslands(self, grid):

    def in_grid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def neighbours(node):
        p, q = node
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        return [(x, y) for x, y in [(p + i, q + j) for i, j in dir] if in_grid(x, y)]

    def dfs(node):
        visited.append(node)
        for v in neighbours(node):
            if grid[v[0]][v[1]]== "1" and v not in visited:
                dfs(v)

    components = 0
    visited = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            node = (i, j)
            if grid[i][j] == "1" and node not in visited:
                components += 1
                dfs(node)

    return components
if __name__ == '__main__':
    grid = """11000
    11000
    00100
    00011"""

    grid = [list(line) for line in grid.splitlines()]
    print(Solution().numIslands(grid))