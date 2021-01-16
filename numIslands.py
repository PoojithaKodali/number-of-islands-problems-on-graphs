class Solution:
    def numIslands(self, box: List[List[str]]) -> int:
        def backtrack(box,i,j,r,c):
            
            if i>=r or j>=c or i<0 or j<0:
                return
            
            if box[i][j]=="2" or box[i][j]=="0":
                return
            
            box[i][j]="2"
            
            backtrack(box,i+1,j,r,c)
            backtrack(box,i-1,j,r,c)
            backtrack(box,i,j+1,r,c)
            backtrack(box,i,j-1,r,c)
            
            return              
            
        r = len(box)
        c = len(box[0])
        
        total = 0
        
        for i in range(r):
            for j in range(c):
                if  box[i][j]=="1":
                    backtrack(box,i,j,r,c)
                    total+=1
        
        return total
        
