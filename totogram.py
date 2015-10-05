__author__ = 'USER'
# BRIEF APPROACH (Used local search and branch and bound techniques)
# 1) Take mid node as root and divide the totogram into three equal sub trees
# -- The first tree takes input a list in the reverse order
# -- The second tree takes as input binary search tree with using Breadth first traversal
# -- The third tree takes as input in ascending order list
# 2) A final list is created of all the three lists with root node in BFS manner
# 3) A dictionary is created to store the parent and children
# 4) Maximum difference edge is calculated and two nodes are sent to selectneighbour function
# 5) Select neighbour checks two neighbours of 1st and two neighbours of 2nd node For instance:
# nodes (1, 9) --diff = 8(maximum) --neighbours of 1 --->2 and neighbours of 9 ---> 8,10
# it then switches the nodes where distance is minimum
# Loop continues till no suitable neighbour is found to be switched

# Reference links :
  #https://www.cs.bu.edu/teaching/c/tree/breadth-first/
  # http://stackoverflow.com/questions/5262308/how-do-implement-a-breadth-first-traversal



# BEST SOLUTION CODE WAS ABLE TO FIND FOR K = 2,3,4,5,6,7
# 1) For k==2
# --> Max value = 2, Time = 0.000999927520752
# --> Tile Arrangement : [2, 1, 3, 4]
# 2) For k==3
# --> Max value = 3, Time = 0.000999927520752
# --> Tile Arrangement : [5, 3, 6, 8, 2, 1, 4, 7, 9, 10]
# 3) For k==4
# --> Max value = 4, Time = 0.000999927520752
# --> Tile Arrangement : [11, 7, 12, 15, 6, 5, 9, 14, 17, 18, 4, 3, 2, 1, 8, 10, 13, 16, 19, 20, 21, 22]
# 4) For k==5
# --> Max value = 6, Time = 0.00399994850159
# --> Tile Arrangement : [23, 17, 24, 29, 14, 13, 19, 28, 33, 34, 12, 11, 9, 7, 16, 21, 26, 31, 35, 36, 38, 40, 10, 8, 6, 5, 4, 3, 2, 1, 15, 18, 20, 22, 25, 27, 30, 32, 37, 39, 41, 42, 43, 44, 45, 46]
# 5) For k==6
# --> Max value = 12, Time = 0.0160000324249
# --> Tile Arrangement : [47, 35, 48, 59, 30, 29, 39, 56, 65, 66, 28, 27, 26, 25, 34, 43, 52, 61, 67, 68, 69, 70, 24, 23, 22, 21, 19, 17, 15, 13, 32, 37, 41, 45, 50, 54, 58, 63, 71, 72, 73, 74, 76, 78, 80, 82, 20, 18, 16, 14, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 31, 33, 36, 38, 40, 42, 44, 46, 49, 51, 53, 55, 57, 60, 62, 64, 75, 77, 79, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]
# 6) For k==7
# --> Max value = 24 Time = 0.140000104904
# --> Tile Arrangement : [95, 71, 96, 119, 62, 61, 79, 112, 129, 130, 60, 59, 58, 57, 70, 87, 104, 121, 131, 132, 133, 134, 56, 55, 54, 53, 52, 51, 50, 49, 66, 75, 83, 91, 100, 108, 116, 125, 135, 136, 137, 138, 139, 140, 141, 142, 48, 47, 46, 45, 44, 43, 42, 41, 39, 37, 35, 33, 31, 29, 27, 25, 64, 68, 73, 77, 81, 85, 89, 93, 98, 102, 106, 110, 114, 118, 123, 127, 143, 144, 145, 146, 147, 148, 149, 150, 152, 154, 156, 158, 160, 162, 164, 166, 40, 38, 36, 34, 32, 30, 28, 26, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 63, 65, 67, 69, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 120, 122, 124, 126, 128, 151, 153, 155, 157, 159, 161, 163, 165, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190]
from math import pow
from collections import defaultdict
import sys
from collections import deque
import time


# Construction of mid Tree
def sort(a, l, h, p):
    low = l
    high = h
    mid = (low + high) / 2
    if high != low:
        p.append(a[mid])
    if low != high and mid != -1 and mid != len(a):
        sort(a, low, mid, p)
        sort(a, mid + 1, high, p)
        return p


# Assigning parents to children (dictionary) using final list
def parentchilddict(final):
    parentchild1 = defaultdict(list)
    final_l = final
    parentchild1[final_l[0]] = [final_l[1], final_l[2], final_l[3]]
    i = 1
    x = ((len(final_l) - 1) / 2)
    while (i < x):
        parentchild1[final_l[i]] = [final_l[2 + (2 * i)], final_l[3 + (2 * i)]]
        i += 1
    return parentchild1


# selecting the next neighbour
def selectneighbour(dict, parorchild, p, n, maximum):
    parchildinfo1 = defaultdict(list)
    parchildinfo1 = dict
    parentorchild = parorchild
    parent = p
    neighbour = n
    max_diff = 999
    neighparent = 0
    for i in parchildinfo1.keys():
        for j in parchildinfo1.get(i):
            if j == neighbour:
                neighparent = i
    if parentorchild in parchildinfo1.keys():
        child = parchildinfo1.get(parentorchild)
        if neighbour in child:
            if abs(neighbour - parent) >= maximum:
                max_diff = abs(neighbour - parent)
        else:
            if neighparent == parent:
                max_diff = 999
            # neighbour is a parent
            elif neighbour in parchildinfo1.keys():
                neighchild = parchildinfo1.get(neighbour)
                if abs(parent - neighbour) < maximum and abs(neighbour - child[0]) < maximum and abs(
                                neighbour - child[1]) < maximum and abs(
                                parentorchild - neighchild[0]) < maximum and abs(
                                parentorchild - neighchild[1]) < maximum and abs(neighparent - parentorchild) < maximum:
                    max_list = [abs(parent - neighbour), abs(neighbour - child[0]), abs(neighbour - child[1]),
                                abs(parentorchild - neighchild[0]), abs(parentorchild - neighchild[1]),
                                abs(neighparent - parentorchild)]
                    max_diff = max(max_list)
            # neighbour is child
            else:
                if abs(parent - neighbour) < maximum and abs(neighbour - child[0]) < maximum and abs(
                                neighbour - child[1]) < maximum and abs(neighparent - parentorchild) < maximum:
                    max_list1 = [abs(parent - neighbour), abs(neighbour - child[0]), abs(neighbour - child[1]),
                                 abs(neighparent - parentorchild)]
                    max_diff = max(max_list1)
    else:
        if neighparent == parent:
            max_diff = 999
        # neighbour is a parent
        elif neighbour in parchildinfo1.keys():
            neighchild = parchildinfo1.get(neighbour)
            if abs(parent - neighbour) < maximum and abs(parentorchild - neighchild[0]) < maximum and abs(
                            parentorchild - neighchild[1]) < maximum and abs(neighparent - parentorchild) < maximum:
                max_diff = max(abs(parent - neighbour), abs(parentorchild - neighchild[0]),
                               abs(parentorchild - neighchild[1]), abs(neighparent - parentorchild))
                # neighbour is child
            else:
                if abs(parent - neighbour) < maximum and abs(neighparent - parentorchild) < maximum:
                    max_diff = max(abs(parent - neighbour), abs(neighparent - parentorchild))
    return max_diff


class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if (self.value == data):
            return self
        elif self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def __str__(self):

        return str(self.value)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def breathFirstSearch(self, root1):
        testqueue = deque()
        testqueue.append(root1)
        output = []
        while len(testqueue) > 0:
            node = testqueue.popleft()
            output.append(str(node))
            if node.left != None:
                testqueue.append(node.left)
            if (node.right != None):
                testqueue.append(node.right)
        return output


if __name__ == '__main__':
    # nodes formation
    if len(sys.argv) == 2:
      k = int(sys.argv[1])
    else:
      print("Missing input argument\n")
      print("USSAGE: python totogram.py [k value]")
      sys.exit()
    start = time.time()
    nodes = 3 * (pow(2, k - 1) - 1) + 1
    nodes = int(nodes)
    # midDFS function
    a = []
    for i in range(1, nodes + 1):
        a.append(i)
    # assigning and removing middle root node
    mid = (0 + nodes) / 2
    root = a[mid - 1]
    a.remove(root)
    # divide into 3 sections (3 Balanced binary tree)
    factor = (len(a)) / 3
    leftBFS = a[0:factor]
    midDFS = a[factor:2 * factor]
    rightBFS = a[2 * factor:3 * factor]
    bst = Tree()
    leftBFS = leftBFS[::-1]
    p = []
    if k == 2:
        midBFS = [3]
    else:
        midDFS = sort(midDFS, 0, len(midDFS), p)
        for i in midDFS:
            bst.insert(i)
        node11 = bst.find(midDFS[0])
        out2 = bst.breathFirstSearch(node11)
        midBFS = map(int, out2)

    final_list = [root]
    level = 1
    max_num = 1
    min_num = 0
    while level != k:
        sub_left = leftBFS[min_num:max_num]
        sub_mid = midBFS[min_num:max_num]
        sub_right = rightBFS[min_num:max_num]
        final_list.extend(sub_left)
        final_list.extend(sub_mid)
        final_list.extend(sub_right)
        min_num = max_num
        max_num = max_num + int(pow(2, level))
        level += 1
    parchildinfo = defaultdict(list)

    while True:
        parchildinfo = parentchilddict(final_list)
        maximum = 0
        selected = -1
        # for maximum value in dictionary
        for i in parchildinfo.keys():
            for j in parchildinfo.get(i):
                maximum1 = abs(j - i)
                if abs(j - i) >= k and maximum1 >= maximum:
                    parent = i
                    parentorchild = j
                    maximum = maximum1
        if maximum == k:
            break
        grandparent = 0
        # finding grandparent of parent
        if parent != root:
            for i in parchildinfo.keys():
                for j in parchildinfo.get(i):
                    if j == parent:
                        grandparent = i
        # neighbours
        n1 = parent - 1
        n2 = parent + 1
        n3 = parentorchild - 1
        n4 = parentorchild + 1
        # neighbours of parent
        if parent == root:
            max1 = 999
            max2 = 999
        elif parent == len(final_list):
            max2 = 999
            max1 = selectneighbour(parchildinfo, parent, grandparent, n1, maximum)
        elif parent == 1:
            max1 = 999
            max2 = selectneighbour(parchildinfo, parent, grandparent, n2, maximum)
        else:
            max1 = selectneighbour(parchildinfo, parent, grandparent, n1, maximum)
            max2 = selectneighbour(parchildinfo, parent, grandparent, n2, maximum)
        # neighbours of child
        if parentorchild == 1:
            max3 = 999
            max4 = selectneighbour(parchildinfo, parentorchild, parent, n4, maximum)
        elif parentorchild == len(final_list):
            max4 = 999
            max3 = selectneighbour(parchildinfo, parentorchild, parent, n3, maximum)
        else:
            max3 = selectneighbour(parchildinfo, parentorchild, parent, n3, maximum)
            max4 = selectneighbour(parchildinfo, parentorchild, parent, n4, maximum)

        if max1 <= max2 and max1 <= max3 and max1 <= max4 and max1 != 999:
            selected = n1
        if max2 <= max1 and max2 <= max3 and max2 <= max4 and max2 != 999:
            selected = n2
        if max3 <= max1 and max3 <= max2 and max3 <= max4 and max3 != 999:
            selected = n3
        if max4 <= max1 and max4 <= max2 and max4 <= max3 and max4 != 999:
            selected = n4

        if selected == -1 and maximum >= k:
            break
        if selected == n1 or selected == n2:
            x, y = final_list.index(parent), final_list.index(selected)
            final_list[y], final_list[x] = final_list[x], final_list[y]
        if selected == n3 or selected == n4:
            x, y = final_list.index(parentorchild), final_list.index(selected)
            final_list[y], final_list[x] = final_list[x], final_list[y]
        del parchildinfo

print maximum
print final_list
end = time.time()
#print end - start
