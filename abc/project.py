import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

import sys
sys.path.insert(0, '../')

from utils import Gym

def select(probabilities, size):
    chosen = []
    for n in np.arange(size):
        r = np.random.rand()
        for i in np.arange(len(probabilities)):
            if r <= probabilities[i]:
                chosen.append(i)
                break
    return chosen


maxIter = 500

gym = Gym(mapX = 100, mapY = 100, startPos = [0, 0], destPos = [100, 100], step = 2, color = 'r', iter = maxIter)


display = 100
foodSourceSize = 100
foodSourceCount = 30
limitforScout = 50

employedBeeCount = 20
onlookerBeeCount = 20

foodSources = np.random.random((foodSourceCount, foodSourceSize))
trialScores = np.zeros(foodSourceCount)

for iter in np.arange(maxIter):
    indexes = np.random.randint(foodSourceCount, size=employedBeeCount)

    # Employed Bees
    for i in indexes:

        k = np.random.randint(foodSourceCount)
        j = np.random.randint(foodSourceSize)
        fi = np.random.uniform(-1, 1)

        newFoodSource = np.copy(foodSources[i])
        alternateFoodSource = foodSources[k]
        newFoodSource[j] = newFoodSource[j] + fi * (newFoodSource[j] - alternateFoodSource[j])

        if newFoodSource[j] < 0:
            newFoodSource[j] = 0
        if newFoodSource[j] > 1:
            newFoodSource[j] = 1

        oldScore = gym.checkSolution(foodSources[i])
        newScore = gym.checkSolution(newFoodSource)

        if newScore < oldScore:
            foodSources[i] = newFoodSource
            trialScores[i] = 0
        else:
            trialScores[i] += 1

    fitnessScores = []
    relativeFitness = []

    scoreSum = 0

    fitnessScores = [gym.checkSolution(foodSource) for foodSource in foodSources]
    scoreSum = sum(fitnessScores)
    relativeFitness = [score / scoreSum for score in fitnessScores]
    probabilities = [sum(relativeFitness[:i+1]) for i in range(len(relativeFitness))]

    indexes = select(probabilities, onlookerBeeCount)

    # Onlooker Bees
    for i in indexes:

        k = np.random.randint(foodSourceCount)
        j = np.random.randint(foodSourceSize)
        fi = np.random.uniform(-1, 1)

        newFoodSource = np.copy(foodSources[i])
        alternateFoodSource = foodSources[k]
        newFoodSource[j] = newFoodSource[j] + fi * (newFoodSource[j] - alternateFoodSource[j])

        if newFoodSource[j] < 0:
            newFoodSource[j] = 0
        if newFoodSource[j] > 1:
            newFoodSource[j] = 1

        oldScore = gym.checkSolution(foodSources[i])
        newScore = gym.checkSolution(newFoodSource)

        if newScore < oldScore:
            foodSources[i] = newFoodSource
            trialScores[i] = 0
        else:
            trialScores[i] += 1

    # Scout Bees
    for idx in np.arange(len(trialScores)):
        if trialScores[idx] > limitforScout:
            foodSources[idx] = np.random.random(foodSourceSize)
            trialScores[idx] = 0

    bestIndexes = np.asarray(fitnessScores).argsort()
    bestFoodSource = foodSources[bestIndexes[0]]

    print('Iteration:', iter, ' - Loss: ',  fitnessScores[0])

    # draw best loss
    gym.addLoss(iter, fitnessScores[0])
    # draw best solution
    gym.drawSolution(iter, bestFoodSource)
