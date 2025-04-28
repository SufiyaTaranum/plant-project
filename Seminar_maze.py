from pyamaze import maze,agent

def RCW():
    global direction
    k=list(direction.keys())
    v=list(direction.values())
    v_rotated=[v[-1]]+v[:-1]

    direction=dict(zip(k,v_rotated))

def RCCW():
    global direction
    k=list(direction.keys())
    v=list(direction.values())
    v_rotated=v[1:]+[v[0]]
    direction=dict(zip(k,v_rotated))

def moveForward(cell):
    if direction['forward']=='E':
        return (cell[0],cell[1]+1),'E'
    if direction['forward']=='W':
        return (cell[0],cell[1]-1),'W'
    if direction['forward']=='N':
        return (cell[0]-1,cell[1]),'N'
    if direction['forward']=='S':
        return (cell[0]+1,cell[1]),'S'

def wallFollower(m):
    global direction
    direction={'forward':'N','left':'W','right':'E','back':'S'}
    currCell=(m.rows,m.cols)
    path=''
    while True:
        if currCell==(1,1):
            break
        if m.maze_map[currCell][direction['left']]==0:
            if m.maze_map[currCell][direction['forward']]==0:
                RCW()
            else:
                currCell,d=moveForward(currCell)
                path+=d
        else:
            RCCW()
            currCell,d=moveForward(currCell)
            path+=d
    return path  
     
    

if __name__=='__main__':
    myMaze=maze(6,6)
    myMaze.CreateMaze()
    a=agent(myMaze,shape='arrow',footprints=True)
    path=wallFollower(myMaze)
    myMaze.run()
    myMaze.tracePath({a:path})

