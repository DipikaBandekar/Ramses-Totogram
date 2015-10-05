__author__ = 'Shwetha'

'''
Ramses revolves around the concept of optimal play betweeen two players playing with the same pieces 'X'.
1. We start the game by storing the 3 command line arguments
   # n - the size of the board which will be n*n
   # array - this stores the current input board state of the game
   # times - will store the time limit within which it has to return an optimal solution

2. We follow the concept of optimal play between the two players Player1 and Player2 by considering the various states that are possible from the given board state and
   try to get the most optimal path by always maximising the values considered as the player must be the one who is supposed to have the maximum score.We further limit the various redundancies and
   additional costs through the process of alpha beta pruning wherein the alpha value and beta value denotes the maximum and minimum limits for the expanded goal state and if the current expanded node
   provides a better prospect we choose it and prune the rest which do not qualify.
3. The game proceeds by looking up the various available moves and the n proceeds to proceed getting the most optimal solution by doing minmax with alpha beta pruning to get the best optimal state for the next move.
4. The time limit is taken into consideration by getting the current time at the beginning of execution and also getting the current time at each level of expansion of the child states and if the time difference exceeds
   the time limit mentioned at command line then the expansion stops and breaks and displays the next optimal move from the best states that have been chosen so far.
5. We display the board state to the user after making the suggested optimal move.
6. Reference links:
   http://neverstopbuilding.com/minimax
   https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

'''



import sys
import random
import time


(n, array, times) = sys.argv[1:]
n=int(n)
currenttime=(time.time())

class Progress(object):

   lose_combinations=[]
   rows=[]
   spaces=()

   #Finding the various combinations for lose state to compare and avoid choosing them
   for i in range(0,n):
       rows=[]
       for j in range(0,n):
           rows.append(n*i+j)
       lose_combinations.append(rows)


   for i in range(0,n):
       rows=[]
       for j in range(0,n):
          rows.append((j*n)+i)
       lose_combinations.append(rows)

   a=[]
   for j in range(0,n):
           a.append(j+(n*j))
   lose_combinations.append(a)

   b=[]
   for j in range(0,n):
           b.append((n-1)*(j+1))
   lose_combinations.append(b)
  # print lose_combinations


   def initialize(self, spaces=()):
        if len(spaces) == 0:
            self.spaces = [None for i in range(n)]
        else:
            self.spaces = spaces
      #  print "Actual Evaluations"+str(self.spaces)

   def openmoves(self):
        row=[]
        for i in range(0,n*n):
           # for j in range(0,n):
                if self.spaces[0][i] is None:
                     row.append(i)
        return row

        '''
        for k, v in enumerate(self.spaces):
           for r in range(0,len(v)):
               if v[r] is None:
                   print r
                   ct=ct+1
        return ct
        '''

   def make_move(self, position, player):
        """place on square on the board"""
        self.spaces[0][position] = player
       # print self.spaces

   def showboard(self):
        # for i in range(0,n):
        #  for k in range(0,n):
        #   print board[i][k]
        rsult=""
        for element in [self.spaces[i:i + n] for i in range(0, len(self.spaces), n)]:
            for ele in range(0,n*n):
                 if element[i][ele]==None:
                    rsult+="."
                 else:
                     rsult+="X"
        print rsult

   def complete(self):
        """is the game over?"""
        if self.loser() != None:
            return True
        return False

   def loser(self):
            positions=[]
            for i in range(0,n):
                row=[]
                for j in range(0,n):
                    row.append(self.spaces[0][n*i+j])
                positions.append(row)

                row=[]
                for j in range(0,n):
                   row.append(self.spaces[0][(j*n)+i])
                positions.append(row)

                row=[]
                for j in range(0,n):
                    row.append(self.spaces[0][j+(n*j)])
                positions.append(row)

                row=[]
                for j in range(0,n):
                   row.append(self.spaces[0][(n-1)*(j+1)])
                positions.append(row)
           # print "inpt board "
            #print positions
            for combo in self.lose_combinations:
                win = True
                #for pos in combo:
                if combo not in positions:
                   win = False
                if win:
                     return player
                  #  print "win is true"
                  #  return True
            return None



   def LosingPlayer(self):
        return self.loser() == 'X'


   def alphabeta(self, node, player, alpha, beta):
        if node.complete():
            if node.LosingPlayer():
                #print "found losing strategy"
                return -1
            else:
                return 1
        for move in node.openmoves():
            node.make_move(move, player)
            val = self.alphabeta(node, player, alpha, beta)
         #   print "val is"+str(val)
            node.make_move(move, None)
            if player == 'X':
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if player == 'X':
            return alpha

def evaluatePlay(obj):
     a = 0
     possibleStates = []
    # print obj.openmoves()

     if len(obj.openmoves()) == (n*n):
        return n+1

     for move in obj.openmoves():
        obj.make_move(move, player)
       # print obj.spaces
        depth=0
        val = obj.alphabeta(obj,player,0,0)
       # print val

        obj.make_move(move, None)
        if val > a:
            a = val
            possibleStates = [move]
        elif val == a:
            possibleStates.append(move)
        timediff=(time.time())-(currenttime)
        if((timediff-currenttime)>times):
            print timediff-currenttime
            break
     #print "available possibleStates"+str(possibleStates)
     return random.choice(possibleStates)

def getboardconfiguration():
     for i in range(0,n*n):
          if(array[i]=='.'):
               row.append(None)
          else:
            row.append(i)
     board.append(row)
     return board


if __name__ == "__main__":

  if(n*n!=len(array)):
      print "Please check your  input as the state of the board and the value of n do not match "
  else:
    board=[]
    row=[]
    player = 'X'
    count=0
    game=Progress()
    board=getboardconfiguration()
    game.initialize(board)
    print "The given board state is:\n"
    game.showboard()

    #while not game.complete():
    if game.complete():
        print "\nGame over as there are no more open moves"
    else:
        computer_move = evaluatePlay(game)
       # print "computer move is "+ str(computer_move)
        row=0
        col=0
        for i in range(0,n):
           for j in range(0,n):
               if computer_move==(n*i+j):
                   row=str(i+1)
                   col=str(j+1)
        game.make_move(computer_move, player)
        if(game.complete()):
            print "The game is out of moves"
        else:
           print "\nHmm, I'd recommend putting your pebble at row "+ row+" and at column "+ col
           print "\nNew Board:\n"
        game.showboard()


















