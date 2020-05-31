def valid(board,num,row,column):
    #column check
    for i in range(len(board[0])):
        if(board[row][i]==num and i!=column):
            return(False)
    #row check
    for i in range(len(board)):
        if(board[i][column]==num and i!=row):
            return(False)
    #box check
    box_x=row//3
    box_y=column//3
    for i in range(box_x*3,box_x*3+3):
        for j in range(box_y*3,box_y*3+3):
            if(board[i][j]==num and i!=row and j!=column):
                return(False)
    return(True)

def find_empty(boa):
    for i in range(len(boa)):
        for j in range(len(boa[0])):
            if(boa[i][j]==0):
                return(i,j)
    return(None)
def solve(board):
    find=find_empty(board)
    if(find==None):
        return("completed solving")
    else:
        row,column=find[0],find[1]
        for i in range(1,10):
            if(valid(board,i,row,column)==True):
                board[row][column]=i
                if(solve(board)):
                    return(True)
                else:
                    board[row][column]=0
        return(False)
board1=[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
solve(board1)
print(board1)
for i in range(len(board1)):
    if(i%3==0):
        print("------------------------")
    for j in range(len(board1[0])):
        if(j%3==0):
            
            print("|",end=" ")
        print(board1[i][j],end=" ")
    print("\n")
