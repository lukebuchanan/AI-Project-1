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
        Returns the start state for the search problem.
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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST

    stack = util.Stack()
    position = problem.getStartState()
    visited = []
    path = []

    # def dfs(successor):
    #     if (problem.isGoalState(successor[0]) == True):
    #         return

    #     for x in problem.getSuccessors(successor[0]):
    #         if(x[0] not in visited):
    #             visited.append(successor[0])
    #             stack.push(x)

    #     dfs(stack.pop())

    #     if(successor[1] == 'North'):
    #         path.append(n)
    #     elif(successor[1] == 'West'):
    #         path.append(w)
    #     elif(successor[1] == 'East'):
    #         path.append(e)
    #     elif(successor[1] == 'South'):
    #         path.append(s)

    # for x in problem.getSuccessors(problem.getStartState()):
    #     stack.push(x)
    # dfs(stack.pop())
    # path.reverse()
        
    #whati fi  just try this shit
    q = util.Stack()
    pos = problem.getStartState()
    for x in problem.getSuccessors(pos):
        q.push(x)
        visited.append(x[0])
        break

    while not q.isEmpty():
        node = q.pop()
        print(node)
        if problem.isGoalState(node[0]):
            break
        s = problem.getSuccessors(node[0])
        for y in s:
            if y[0] not in visited:
                q.push(y)
                visited.append(y[0])
                break

    # while True:
    #     #if here break
    #     #set position as visited
    #     visited.append(position)
    #     for x in problem.getSuccessors(position):
    #         if(x[0] not in visited):
    #             stack.push(x)

    #     #set the next node to visit
    #     successor = stack.pop()
    #     print(successor)
    #     position = successor[0]
    #     #if position not in successors of cur pos dont add it to path
    #     if(successor[1] == 'North'):
    #         path.append(n)
    #     elif(successor[1] == 'West'):
    #         path.append(w)
    #     elif(successor[1] == 'East'):
    #         path.append(e)
    #     elif(successor[1] == 'South'):
    #         path.append(s)

    return path

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
