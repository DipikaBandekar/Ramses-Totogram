'''
Formulation of search problem:
1)BFS: We have used FIFO approach and we are maintaining visited nodes and we are popping
2)DFS: We have used LIFO approach and we are maintaining visited nodes
'''

from collections import defaultdict
from math import radians,sin,cos,asin,sqrt

# https://pypi.python.org/pypi/haversine, http://rosettacode.org/wiki/Haversine_formula#Python
def heurist(current_city,end_city):
    lat1 = 0.0
    lat2 = 0.0
    long1 = 0.0
    long2 = 0.0
    document = open('city-gps.txt', 'r')
    line = document.readline()
    while (line):
        split = line.split(' ')
        if (split[0] == current_city):
            lat1,long1 = float(split[1]),float(split[2])
        if (split[0] == end_city):
            lat2,long2 = float(split[1]),float(split[2])
        line = document.readline()
    document.close()
    R = 6371 # Earth radius in kilometers
    dLat = radians(lat2 - lat1)
    dLon = radians(long2 - long1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    heuristic = (R * c)*0.621371
    return heuristic

# To display the child nodes information of distance, speed and Highways --> Used calculating parameters
def childDict(parent):
    childdict = defaultdict(dict)
    document = open('road-segments.txt', 'r')
    line = document.readline()
    while (line):
        splitarray = line.split(' ')
        if splitarray[0] == parent:
            childdict[splitarray[0]][splitarray[1]] = [splitarray[2], splitarray[3], splitarray[4]]
        line = document.readline()
    document.close()
    return childdict


# To display the child nodes of any given node --> Used in BFS DFS algorithms
def childNode(parent1):
    childlist = []
    document = open('road-segments.txt', 'r')
    line = document.readline()
    while (line):
        split = line.split(' ')
        if (split[0] == parent1):
            childlist.append(split[1])
        line = document.readline()
    document.close()
    return childlist


# Used to calculate BFS/DFS Total distance, speed and highways traversed
def calculate_parameters(visited):
    speed = 0.0
    dist = 0.0
    time = 0.0
    highway = []
    n = 0
    m = 1
    childinfo = defaultdict(dict)
    while m < len(visited):
        childinfo = childDict(visited[n])
        for i in childinfo:
            inner_key = childinfo[i].keys()
            for j in inner_key:
                if j in visited:
                    dspeedh = childinfo[i][j]
                    dist = dist + float(dspeedh[0])
                    if type(float(dspeedh[1])) is float:
                        speed = speed + float(dspeedh[1])
                    if dspeedh[2] in dspeedh or type(float(dspeedh[1])) is str:
                        highway.append(dspeedh[2])
        n += 1
        m += 1
    time = round(dist / speed, 2)
    dsh = [dist, time, highway]
    return dsh


# BFS Algorithm
def bfs(source, target,opt):
    print "Source:", source, "--> Target:", target
    queue = [source]
    visited = []
    graph = []
    dist = 0.0
    time = 0.0
    highway = []
    final_list = []
    while len(queue) > 0:
        node = queue.pop(0)
        graph = childNode(node)
        if node == target:
            visited.append(node)
            break
        elif node not in visited:
            visited = visited + [node]
        if graph is not None:
            queue = queue + graph
    dthlist = calculate_parameters(visited)
    dist = dthlist[0]
    time = dthlist[1]
    highway = dthlist[2]
    edges = len(visited) - 1
    print "The highways used to travel from ",source," to ",target,"are",highway
    if (opt==1):
        print "Total turns taken: ",edges
    if(opt==2):
        print "Total distance covered: ",dist
    if(opt==3):
        print "Time required in hours: ",time
    print "List of cities visited: ",visited
    final_list = [dist, time, visited]
    return final_list

# DFS Algorithm
def dfs(source, target,opt):
    print "Source:", source, "--> Target:", target
    stack = [source]
    visited = []
    graph = []
    dist = 0.0
    time = 0.0
    highway = []
    final_list = []
    while len(stack) > 0:
        node = stack.pop(0)
        graph = childNode(node)
        if node == target:
            visited.append(node)
            break
        elif node not in visited:
            visited = visited + [node]
        if graph is not None:
            stack = graph + stack
    dthlist = calculate_parameters(visited)
    dist = dthlist[0]
    time = dthlist[1]
    highway = dthlist[2]
    edges = len(visited) - 1
    print "The highways used to travel from ",source," to ",target,"are",highway
    if (opt==1):
        print "Total turns taken: ",edges
    if(opt==2):
        print "Total distance covered: ",dist
    if(opt==3):
        print "Time required in hours: ",time
    print "List of cities visited: ",visited
    final_list = [dist, time, visited]
    return final_list

# Used to produce child nodes for A* Algorithm in sorted order based on routing option(time/distance)
def childastar(parentnode, opt):
    node = parentnode
    childnodes = []
    parameter = []
    childinfo = defaultdict(dict)
    document = open('road-segments.txt', 'r')
    line = document.readline()
    while (line):
        splitarray = line.split(' ')
        if (splitarray[0] == parentnode and opt == 2):
            childinfo[splitarray[0]][splitarray[1]] = float(splitarray[2])
        if (splitarray[0] == parentnode and opt == 3 and float(splitarray[3]) is not str):
            childinfo[splitarray[0]][splitarray[1]] = float(splitarray[3])
        if (opt == 1):
            childinfo[splitarray[0]][splitarray[1]] = 1.0
        line = document.readline()
    document.close()
    for i in childinfo[node].keys():
        r = min(childinfo[node], key=childinfo[node].get)
        childnodes.append(r)
        parameter.append(childinfo[node][r])
        if (childinfo[node].keys is not None):
            del childinfo[node][r]
    p = [childnodes, parameter]
    return p

# A* Algorithm function
def astar(source, target, option):
    print "Source:", source, "--> Target:", target
    fringedict = defaultdict(float)
    visited = []
    fringedict = {source: 0.0}
    childnodes = []
    pathcost = 0.0
    dist = 0.0
    distancedict = defaultdict(float)
    distancedict = {source: 0.0}
    total_cost = 0.0
    while len(fringedict.keys()) > 0:
        (' specific condition when target node and other nodes have same costs')
        if target in fringedict.keys():
            node = target
        else:
            q = min(fringedict, key=fringedict.get)
            node = q
        total_cost = fringedict.pop(node)
        dist = distancedict.pop(node)
        if node == target:
            visited.append(node)
            break
        if node not in visited:
            visited.append(node)

        graph = childastar(node, option)
        childnodes = graph[0]
        print graph
        m = 0
        for child in childnodes:
            pathcost = dist + graph[1][m]
            heuristic = heurist(child,target)
            cost = pathcost + heuristic
            m += 1
            fringedict[child] = cost
            distancedict[child] = pathcost
            if child == target:
                break

        #dthlist = calculate_parameters(visited)
        #highway = dthlist[2]
        edges = len(visited) - 1
   # print "The highways used to travel from ",source," to ",target,"are",highway
    if (option==1):
        print "Total turns taken: ",total_cost
    if(option==2):
        print "Total distance covered: ",total_cost
    if(option==3):
        print "Speed required in miles: ",total_cost
    print "List of cities visited: ",visited
    final_list = [total_cost, visited]
    return final_list

# Main Function
if __name__ == '__main__':

    #print astar('"Y"_City,_Arkansas', 'Page,_Oklahoma', 1)
    #start_city = input('Enter City 1: ')
    #end_city = input('Enter City 2: ')
    start_city = '"Y"_City,_Arkansas'
    end_city = 'Page,_Oklahoma'
    option = input('Enter Routing Option:\n1. Press 1 for Segements\n2. Press 2 for Distance\n3. Press 3 for Time\n')
    A = [1,2,3]
    if option not in A:
        print "Invalid Option"
    algo = input('Enter Routing Algorithm:\n1. Press 1 for BFS\n2. Press 2 for DFS\n3. Press 3 for A*\n')
    if algo not in A:
        print "Invalid Option"
    if(algo==1):
        print bfs(start_city,end_city,option)
    if(algo==2):
        print dfs(start_city,end_city,option)
    if(algo==3):
        print astar(start_city,end_city,option)

