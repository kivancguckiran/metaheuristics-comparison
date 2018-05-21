import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

import sys
sys.path.insert(0, '../')

from utils import Gym


maxIter = 500

gym = Gym(mapX = 100, mapY = 100, startPos = [0, 0], destPos = [100, 100], step = 2, color = 'r', iter = maxIter)

geneSize = 100
populationSize = 30
breederCount = 10
mutationChance = 0.01

population = np.random.random((populationSize, geneSize))

for iter in np.arange(maxIter):
    fitnessScores = []

    for individual in population:
        fitnessScores.append(gym.checkSolution(individual))

    bestIndexes = np.asarray(fitnessScores).argsort()
    bestIndividual = population[bestIndexes[0]]
    bestIndividualScore = fitnessScores[bestIndexes[0]]
    breederIndexes = bestIndexes[:breederCount]
    breederIndexes = np.reshape(breederIndexes, (int(breederCount / 2), 2))

    print('Iteration:', iter, ' - Loss: ',  bestIndividualScore)

    # draw best loss
    gym.addLoss(iter, bestIndividualScore)
    # draw best solution
    gym.drawSolution(iter, bestIndividual)

    newPopulation = []

    for index in breederIndexes:
        father = population[index[0]]
        mother = population[index[1]]

        pos = int(np.random.random() * geneSize)

        child1 = np.concatenate((father[:pos], mother[pos:]), axis=0)
        child2 = np.concatenate((father[pos:], mother[:pos]), axis=0)

        for i in np.arange(len(child1)):
            if mutationChance > np.random.random():
                child1[i] = np.random.random()
        for i in np.arange(len(child2)):
            if mutationChance > np.random.random():
                child2[i] = np.random.random()

        newPopulation.append(father)
        newPopulation.append(mother)
        newPopulation.append(child1)
        newPopulation.append(child2)

    np.random.shuffle(newPopulation)

    population = newPopulation


