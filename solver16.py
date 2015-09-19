__author__ = 'USER'
'''

'''
from collections import defaultdict

# Heuristic function of no. of tiles in the wrong location is used
def heurist(matrix):
    state = matrix
    h = 0
    m = 0
    n = 0
    value = 1
    # comparing each tile with goal tile
    for i in state:
        n = 0
        for j in i:
            if n < 4 and m < 4:
                if state[m][n] != value:
                    h += 1
            n += 1
            value += 1
        m += 1
    return h
# finding 16 states
def findstates(matrix,depth):
   parent=[]
   leveldict=defaultdict(list)


   #left
   for level in range(0,4):
     temprow=[]
     newval=[]
     parent=[]
     #zeroth level
     if(level==0):
        newval=[]
        for j in range(0 ,4):
          if(j!=3):
            newval.append(matrix[level][j+1])
          else:
           newval.append(matrix[level][0])
        parent.append(list(newval))
        for i in range(level+1,4):
            temprow=[]
            for j in range(0,4):
             temprow.append(matrix[i][j])
            parent.append(list(temprow))

     #to get the rows of same values if level is higher than 0
     if(level>0):
         parent=[]
         for i in range(0,level):
            temprow=[]
            for j in range(0,4):
             temprow.append(matrix[i][j])
            parent.append(list(temprow))
       #to get the row of reversion
         newval=[]
         for j in range(0 ,4):
          if(j!=3):
            newval.append(matrix[level][j+1])
          else:
            newval.append(matrix[level][0])
         parent.append(list(newval))
         newval=[]
     #to get the remaining rows
     if(level>0):
         for i in range(level+1,4):
            newval=[]
            for j in range(0,4):
             newval.append(matrix[i][j])
            parent.append(newval)
     keyval='level'+str(depth)+'L'+str(level)
     leveldict[keyval]=parent

   #direction right
  #if(direction)=="right":
   for level in range(0,4):
     temprow=[]
     newval=[]
     parent=[]
     #zeroth level
     if(level==0):
        newval=[]
        for j in range(0 ,4):
          if(j!=0):
            newval.append(matrix[level][j-1])
          else:
           newval.append(matrix[level][3])
        parent.append(list(newval))
        for i in range(level+1,4):
            temprow=[]
            for j in range(0,4):
             temprow.append(matrix[i][j])
            parent.append(list(temprow))

     #to get the rows of same values if level is higher than 0
     if(level>0):
         parent=[]
         for i in range(0,level):
            temprow=[]
            for j in range(0,4):
             temprow.append(matrix[i][j])
            parent.append(list(temprow))
       #to get the row of reversion
         newval=[]
         for j in range(0 ,4):
          if(j!=0):
            newval.append(matrix[level][j-1])
          else:
            newval.append(matrix[level][3])
         parent.append(list(newval))
         newval=[]
     #to get the remaining rows
     if(level>0):
         for i in range(level+1,4):
            newval=[]
            for j in range(0,4):
             newval.append(matrix[i][j])
            parent.append(newval)
     keyval='level'+str(depth)+'R'+str(level)
     leveldict[keyval]=parent

   #up
   for level in range(0,4):
      row=[]
      longlist=[]
      newMatrix=[]
      tempMatrix=[]
      for i in range(0,4):
          row=[]
          for j in range(0,4):
              row.append(matrix[i][j])
              longlist.append(matrix[i][j])
          newMatrix.append(row)
      print newMatrix
      for i in range(0,4):
          if(i!=3):
            newMatrix[i][level]=matrix[i+1][level]
          else:
            newMatrix[i][level]=matrix[level][level]

      keyval='level'+str(depth)+'U'+str(level)
      leveldict[keyval]=newMatrix

    #down
   for level in range(0,4):
      row=[]
      longlist=[]
      newMatrix=[]
      tempMatrix=[]
      for i in range(0,4):
          row=[]
          for j in range(0,4):
              row.append(matrix[i][j])
              longlist.append(matrix[i][j])
          newMatrix.append(row)
      print newMatrix
      for i in range(0,4):
          if(i!=0):
            newMatrix[i][level]=matrix[i-1][level]
          else:
            newMatrix[i][level]=matrix[3][level]

      keyval='level'+str(depth)+'D'+str(level)
      leveldict[keyval]=newMatrix

   return leveldict

# A* function to calculate the minimum cost
def astar(initial_matrix):
    initial = 'I'
    final = 'F'
    i_matrix = initial_matrix
    target = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # --fringe dictionary to keep track of nodes and their costs in order to select node with minimum cost
    fringedict = defaultdict(int)
    # --Heuristic dictionary to keep track of all states and their matrices or states
    heuristicdict = defaultdict(list)
    states = defaultdict(list)
    # --visited to display the nodes expanded
    visited = []
    fringedict = {initial: 0}
    heuristicdict = {initial: i_matrix}
    distancedict = defaultdict(int)
    distancedict = {initial: 0}
    childnodes = []
    pathcost = 0
    dist = 0
    level = 1
    while len(fringedict.keys()) > 0:
        # --specific condition when final state and other states have same costs
        if final in fringedict.keys():
            node = final
        else:
            # --selecting the node with minimum cost from the fringe dictionary
            q = min(fringedict, key=fringedict.get)
            node = q
            fringedict.pop(node)
            selected_node = heuristicdict.pop(node)
            dist = distancedict.pop(node)

        print node
        if node == final:
            visited.append(node)
            break
        if node not in visited:
            visited.append(node)
        statesdict = findstates(selected_node,level)
        level += 1
        heuristicdict.update(statesdict)
        childnodes = heuristicdict.keys()
        print childnodes
        #--finding child states of expanded node and updating the costs in dictionary
        for child in childnodes:
            pathcost = dist + 1
            child_matrix = heuristicdict.get(child)
            heuristic = heurist(child_matrix)
            cost = pathcost + heuristic
            #--heuristic is 0 when goal state reached
            if heuristic == 0:
                final = child
                fringedict[final] = cost
                break
            else:
                fringedict[child] = cost
                distancedict[child] = pathcost
        print fringedict
    return visited


# Main Function
if __name__ == '__main__':

    input_matrix = []
    document = open('input-board-solver16.txt', 'r')
    line = document.readline()
    m = 0
    while (line):
        split = line.split(' ')
        input_matrix.append([int(split[0]), int(split[1]), int(split[2]), int(split[3])])
        line = document.readline()
    document.close()
    print input_matrix

    expanded_nodes = astar(input_matrix)
    print expanded_nodes
    expanded_nodes.remove('I')
    final_output = []
    n=0
    while n<len(expanded_nodes):
        final_output.append(expanded_nodes[n][6:8])
        n+=1

print final_output

