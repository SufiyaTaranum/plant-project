from pyamaze import maze,agent

myMaze=maze(6,6)
myMaze.CreateMaze()
a=agent(myMaze,shape='arrow',footprints=True)
path='WNNWNNES'
myMaze.tracePath({a:path})
myMaze.run()