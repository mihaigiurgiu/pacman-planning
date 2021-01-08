# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the startLocSet = True state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def generateRandomGrid(size):
    f = open("layouts/randomLayout.lay", "w")

    # first_last = '%' * (size+2)
    # intermediate = '%' + ' ' * size + '%'

    # f.write(first_last + '\n')
    # for i in range(1, size+1):
    #     f.write(intermediate + '\n')
    # f.write(first_last)

    lay = [[' ' for i in range(size+2)] for j in range(size+2)]

    for i in range(0, size+2):
        for j in range(0, size+2):
            if (i == 0 or j == 0 or i == size+1 or j == size+1):
                lay[i][j] = '%'

    from util import random

    maxHoles = (int)((size*size)/2)
    minHoles = (int)((size*size)/6)

    noOfHoles = random.randint(minHoles, maxHoles)
    holesCnt = 0

    startLocSet = False
    restLocSet = False
    destLocSet = False


    for i in range(1, size+1):
        for j in range(1, size+1):
            if(holesCnt != noOfHoles):
                chance = random.randint(1, 100)
                if(chance < 21): 
                    lay[i][j] = 'H'
                    holesCnt += 1
            else:
                break    
        if(holesCnt == noOfHoles):
            break
            

    while (not startLocSet):
        x = random.randint(1, size+1)
        y = random.randint(1, size+1)
        if lay[x][y] == ' ':
            lay[x][y] = 'P'
            startLocSet = True

    while (not restLocSet):
        x = random.randint(1, size+1)
        y = random.randint(1, size+1)
        if lay[x][y] == ' ':
            lay[x][y] = 'R'
            restLocSet = True

    while (not destLocSet):
        x = random.randint(1, size+1)
        y = random.randint(1, size+1)
        if lay[x][y] == ' ':
            lay[x][y] = 'D'
            destLocSet = True

    # for i in range(1, size+1):
    #     for j in range(1, size+1):
    #         if (not startLocSet):
    #             if lay[i][j] == ' ':
    #                 chance = random.randint(1, 100)
    #                 if(chance < 3):
    #                     lay[i][j] = 'P'
    #                     startLocSet = True
    #         else:
    #             break
    #     if startLocSet:
    #         break

    # for i in range(1, size+1):
    #     for j in range(1, size+1):
    #         if (not restLocSet):
    #             if lay[i][j] == ' ':
    #                 chance = random.randint(1, 100)
    #                 if(chance < 3):
    #                     lay[i][j] = 'R'
    #                     restLocSet = True
    #         else: 
    #             break
    #     if restLocSet:
    #         break
                    
    
    # for i in range(1, size+1):
    #     for j in range(1, size+1):
    #         if(not destLocSet):
    #             if lay[i][j] == ' ':
    #                 chance = random.randint(1, 100)
    #                 if(chance < 3):
    #                     lay[i][j] = 'D'
    #                     destLocSet = True
    #         else:
    #             break
    #     if destLocSet:
    #         break
    
    for i in range(0, size+2):
        for j in range(0, size+2):
            f.write(str(lay[i][j]))
        f.write('\n')                

    f.close()

def foodDeliveryPlan(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    generateRandomGrid(30)

    solution = []

    import subprocess
    exitCode = subprocess.call('../fast-downward.py delivery.pddl delivery1.pddl --evaluator "hff=ff()" --search "lazy_greedy([hff], preferred=[hff])"', shell=True)

    if(not exitCode):
        f = open("sas_plan", "r")
        lines = f.readlines()
        f.close()
        for i in range(len(lines)):
            dir = lines[i].split(" ")
            if dir[0] == '(north':
                solution.append(n)
            elif dir[0] == '(south':
                solution.append(s)
            elif dir[0] == '(west':
                solution.append(w)
            elif dir[0] == '(east':
                solution.append(e)
            elif dir[0] == '(pick-up':
                print 'food picked up'

        print solution
        return solution   

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the startLocSet = True a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
