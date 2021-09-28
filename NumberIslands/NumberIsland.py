
def dfs(grid,i,j):
    if (i<0 or j <0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='0' ):
        return 0
    grid[i][j]='0'
    dfs(grid,i+1,j)
    dfs(grid,i-1,j)
    dfs(grid,i,j+1)
    dfs(grid,i,j-1)
    return 1

def numIslands(grid):
    if (grid == None or len(grid) == 0):
        return 0
    numIslands = 0
    for i in range(len(grid)):
        for j in range (len(grid[i])):
            if grid[i][j]=='1':
                numIslands += dfs(grid,i,j)
    return numIslands
                    
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print (numIslands(grid))  


grid = [["1","1","0","1"],["0","0","1","0"],["0","0","0","0"]]
print (numIslands(grid))