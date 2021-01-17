class Solution:
    def __init__(self):
        self.visited = set()# set has o(1) membership finding , hence used set
        
    def is_valid(self, row, column, grid):
        if 0 <= row < len(grid) and 0<= column < len(grid[0]):
            return True
        return False


    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if self.is_valid(sr,sc, image):
            old_color = image[sr][sc]
            direction_vector = [(1,0),(0,1),(-1,0),(0,-1)] # extensible, for this problem we can move in 4 directions
            self.dfs(image, sr,sc, newColor, old_color, direction_vector)
        return image

    def dfs(
        self, 
        image: List[List[int]], 
        row : int , column: int, new_color: int, old_color: int, 
        direction_vector:List
    ):
        image[row][column] = new_color
        self.visited.add((row,column))

        for row_dv, column_dv in direction_vector:
            new_row = row+row_dv
            new_column = column+column_dv
            if self.is_valid(new_row, new_column, image) \
            and image[new_row][new_column]==old_color \
            and (new_row, new_column) not in self.visited:
                self.dfs(image,new_row, new_column, new_color, old_color,direction_vector)
                
        
