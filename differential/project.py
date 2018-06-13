import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

import sys
sys.path.insert(0, '../')

from utils import Gym


maxIter = 500

gym = Gym(mapX = 100, mapY = 100, startPos = [0, 0], destPos = [100, 100], step = 2, color = 'r', iter = maxIter)

maxIter = 500
solutionSize = 100
populationSize = 30
F = 0.1 # 0-2
CR = 0.5 # 0-1

population = np.random.random((populationSize, solutionSize))

for iter in np.arange(maxIter):
    solutionScores = []

    for idx in np.arange(populationSize):
        solution = population[idx]
        newSolution = []

        while True:
            indexes = np.random.choice(populationSize, 3, replace=False)
            if idx not in indexes:
                break

        a = population[indexes[0]]
        b = population[indexes[1]]
        c = population[indexes[2]]

        R = np.random.choice(populationSize)

        for i in np.arange(len(solution)):
            ri = np.random.random()
            
            if ri < CR or i == R:
                newSolution.append(a[i] + F * (b[i] - c[i]))
            else:
                newSolution.append(solution[i])

        newFitness = gym.checkSolution(newSolution)
        oldFitness = gym.checkSolution(solution)

        if newFitness < oldFitness:
            population[idx] = newSolution

        solutionScores.append(gym.checkSolution(population[idx]))

    bestSolutionIdx = solutionScores.index(min(solutionScores))

    print('Iteration:', iter, ' - Loss: ',  solutionScores[bestSolutionIdx])
    # draw best loss
    gym.addLoss(iter, solutionScores[bestSolutionIdx])
    # draw best solution
    gym.drawSolution(iter, population[bestSolutionIdx])


