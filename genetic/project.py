import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines


mapX = 100
mapY = 100
maxIter = 100
display = 1
step = 2
startingPoint = [0, 0]
destinationPoint = [100, 100]

geneSize = 150
populationSize = 30
breederCount = 10
mutationChance = 0.01

population = np.random.random((populationSize, geneSize))

def drawSolution(solution):
    color = 'r'
    newPosition = startingPoint[:]
    lastPosition = startingPoint[:]

    for dir in solution:
        alpha = dir * 2 * np.pi

        newPosition[0] += step * np.cos(alpha)
        newPosition[1] += step * np.sin(alpha)

        if newPosition[0] < 0:
            newPosition[0] = 0
        if newPosition[1] < 0:
            newPosition[1] = 0
        if newPosition[0] > mapX:
            newPosition[0] = mapX
        if newPosition[1] > mapY:
            newPosition[1] = mapY

        x = np.asarray([lastPosition[0], newPosition[0]])
        y = np.asarray([lastPosition[1], newPosition[1]])

        plt.plot(x, y, c=color)

        lastPosition = newPosition[:]

def checkFitness(solution):
    pos = startingPoint[:]

    for dir in solution:
        alpha = dir * 2 * np.pi

        pos[0] += step * np.cos(alpha)
        pos[1] += step * np.sin(alpha)

        if pos[0] < 0:
            pos[0] = 0
        if pos[1] < 0:
            pos[1] = 0
        if pos[0] > mapX:
            pos[0] = mapX
        if pos[1] > mapY:
            pos[1] = mapY

    return np.sqrt(np.square(destinationPoint[1] - pos[1]) + np.square(destinationPoint[0] - pos[0]))

losses = []

for iter in np.arange(maxIter):
    fitnessScores = []

    for individual in population:
        fitnessScores.append(checkFitness(individual))

    bestIndexes = np.asarray(fitnessScores).argsort()
    bestIndividual = population[bestIndexes[0]]
    bestIndividualScore = fitnessScores[bestIndexes[0]]
    breederIndexes = bestIndexes[:breederCount]
    breederIndexes = np.reshape(breederIndexes, (int(breederCount / 2), 2))

    if iter % display == 0:
        print('Iteration ', iter)
        print('Best ', bestIndividualScore)

        losses.append(bestIndividualScore)
        # draw best solution
        plt.cla()
        plt.axis([0, mapX + 1, 0, mapY + 1])

        drawSolution(bestIndividual)

        plt.savefig('images/iter_' + str(iter) + '.png')

        plt.pause(0.1)

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


plt.show()

plt.cla()
plt.plot(losses)
plt.savefig('loss.png')

