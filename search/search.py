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

class Vertice(object):

    def __init__(self, elemento, peso):
        self.coordenadas = elemento[0]
        self.direcao = elemento[1]
        self.peso = peso

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
    """

    grafoBusca = util.Stack()
    visitados = []

    inicialFormat = Vertice([problem.getStartState(), 'Fim'], 0)
    grafoBusca.push(inicialFormat)

    while not grafoBusca.isEmpty():

        atualNo = grafoBusca.pop()

        sucessores = problem.getSuccessors(atualNo.coordenadas)
        visitados.append(atualNo.coordenadas)

        if problem.isGoalState(atualNo.coordenadas):
            return formataSolucao(atualNo)

        for caminho in sucessores:

            novoNo = Vertice(caminho, atualNo.peso + 1)

            if novoNo.coordenadas not in visitados:
                grafoBusca.push(novoNo)
                novoNo.anterior = atualNo

    return formataSolucao(atualNo)


def breadthFirstSearch(problem):
    """Search the node that has the lowest combined cost and heuristic first."""

    grafoBusca = util.Queue()
    visitados = []

    inicialFormat = Vertice([problem.getStartState(), 'Fim'], 0)
    grafoBusca.push(inicialFormat)

    # teste = 0

    while not grafoBusca.isEmpty():

        atualNo = grafoBusca.pop()

        # testeBk = teste
        # teste = 0
        # for x in atualNo.coordenadas[1]:
        #     teste += x
        #
        # if teste > testeBk:
        #     grafoBusca = util.Queue()
        #     visitados = []

        sucessores = problem.getSuccessors(atualNo.coordenadas)
        visitados.append(atualNo.coordenadas)

        if problem.isGoalState(atualNo.coordenadas):
            return formataSolucao(atualNo)

        for caminho in sucessores:

            novoNo = Vertice(caminho, atualNo.peso + 1)

            if novoNo.coordenadas not in visitados:
                grafoBusca.push(novoNo)
                novoNo.anterior = atualNo

    return formataSolucao(atualNo)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""


    grafoBusca = util.PriorityQueue();
    visitados = []

    inicialFormat = Vertice([problem.getStartState(), 'Fim'], 0)
    grafoBusca.push(inicialFormat, 0)

    while not grafoBusca.isEmpty():

        atualNo = grafoBusca.pop()

        sucessores = problem.getSuccessors(atualNo.coordenadas)
        visitados.append(atualNo.coordenadas)

        if problem.isGoalState(atualNo.coordenadas):
            return formataSolucao(atualNo)

        for caminho in sucessores:

            novoNo = Vertice(caminho, atualNo.peso + 1)

            if novoNo.coordenadas not in visitados:
                grafoBusca.push(novoNo, novoNo.peso)
                novoNo.anterior = atualNo

    return formataSolucao(atualNo)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """

    grafoBusca = util.PriorityQueue()
    visitados = []

    inicialFormat = Vertice([problem.getStartState(), 'Fim'], 0)
    grafoBusca.push(inicialFormat, 0)

    while not grafoBusca.isEmpty():

        atualNo = grafoBusca.pop()
        sucessores = problem.getSuccessors(atualNo.coordenadas)
        visitados.append(atualNo.coordenadas)

        if problem.isGoalState(atualNo.coordenadas):
            return formataSolucao(atualNo)

        for caminho in sucessores:

            novoNo = Vertice(caminho, atualNo.peso + 1)

            if novoNo.coordenadas not in visitados:
                grafoBusca.push(novoNo, heuristic(novoNo.coordenadas, problem))
                novoNo.anterior = atualNo

    return -1


def formataSolucao(inicio):

    import collections

    solucao = collections.deque()
    solucao.appendleft(inicio.direcao)

    atualNo = inicio

    while(atualNo.anterior.direcao != 'Fim'):
        solucao.appendleft(atualNo.anterior.direcao)
        atualNo = atualNo.anterior
    return solucao


def learningRealTimeAStar(problem, heuristic=nullHeuristic):
    """Execute a number of trials of LRTA* and return the best plan found."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    # MAXTRIALS = ...
    

# Abbreviations 
# *** DO NOT CHANGE THESE ***
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
lrta = learningRealTimeAStar
