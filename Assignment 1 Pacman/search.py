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
import searchAgents
import game

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
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    open_list = util.Queue()
    closed_list = []
    start_node = (problem.getStartState(), [])

    open_list.push(start_node)

    while not open_list.isEmpty():
        state, action = open_list.pop()

        if state not in closed_list:
            closed_list.append(state)
            if problem.isGoalState(state):
                return action
            for successor in problem.getSuccessors(state):
                next_state, next_action, next_cost = successor
                next_node = (next_state, action + [next_action])
                open_list.push(next_node)

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
    """
    Search the node that has the lowest combined cost and heuristic first.
    You DO NOT need to implement any heuristic, but you DO have to call it.
    The heuristic function is "manhattanHeuristic" from searchAgent.py.
    It will be pass to this function as second argument (heuristic).
    """
    "*** YOUR CODE HERE FOR TASK 2 ***"

    open_list = util.PriorityQueue()
    closed_list = []

    start_state = problem.getStartState()
    start_fn = 0 + heuristic(start_state, problem)
    start_node = (start_state, start_fn, 0, [])

    open_list.push(start_node, start_fn)
    best_g = 0

    while not open_list.isEmpty():
        current_node = open_list.pop()
        state, fn, accum_cost, actions = current_node

        if state not in closed_list or accum_cost < best_g:
            closed_list.append(state)
            best_g = accum_cost

            if problem.isGoalState(state):
                return actions

            for successor in problem.getSuccessors(state):
                next_state, next_action, next_cost = successor

                next_accum_cost = accum_cost + next_cost
                next_heuristic = heuristic(next_state, problem)
                next_fn = next_accum_cost + next_heuristic

                next_node = (next_state, next_fn, next_accum_cost, actions + [next_action])
                open_list.push(next_node, next_fn)
                open_list.update(next_node, next_fn)
    return False

    util.raiseNotDefined()

# Extensions Assignment 1
# Helper function for Enhanced Hill-climbing
def improve(initial_state, problem, heuristic):
    open_list = util.Queue()
    closed_list = []
    open_list.push((initial_state, []))

    while not open_list.isEmpty():
        state, actions = open_list.pop()
        if state not in closed_list:
            closed_list.append(state)
            if heuristic(state, problem) < heuristic(initial_state, problem):
                return state, actions
            for successor in problem.getSuccessors(state):
                next_state, next_action, next_cost = successor
                open_list.push((next_state, actions + [next_action]))
    return False


def enforcedHillClimbing(problem, heuristic=nullHeuristic):
    """
    Local search with heuristic function.
    You DO NOT need to implement any heuristic, but you DO have to call it.
    The heuristic function is "manhattanHeuristic" from searchAgent.py.
    It will be pass to this function as second argument (heuristic).
    """
    "*** YOUR CODE HERE FOR TASK 1 ***"

    final_path = []
    state = problem.getStartState()
    while not problem.isGoalState(state):
        state, path = improve(state, problem, heuristic)
        final_path += path
    return final_path

    util.raiseNotDefined()

    
def jumpPointSearch(problem, heuristic=nullHeuristic):
    """
    Search by pruning non-critical neighbors with jump points.
    You DO NOT need to implement any heuristic, but you DO have to call it.
    The heuristic function is "manhattanHeuristic" from searchAgent.py.
    It will be pass to this function as second argument (heuristic).
    """
    "*** YOUR CODE HERE FOR TASK 3 ***"

    util.raiseNotDefined()



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ehc = enforcedHillClimbing
jps = jumpPointSearch
