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

bandwidth = 0.01
solutionSize = 150
harmonyMemorySize = 30
harmonyMemoryConsiderationRate = 0.99
pitchAdjustRate = 0.01

harmonyMemory = np.random.random((harmonyMemorySize, solutionSize))

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

def checkSolution(solution):
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
    solutionScores = []

    for idx in np.arange(harmonyMemorySize):
        solution = harmonyMemory[idx]

        for i in np.arange(len(solution)):
            if np.random.rand() < harmonyMemoryConsiderationRate:
                if np.random.rand() < pitchAdjustRate:
                    change = bandwidth * np.random.rand()
                    if np.random.rand() < 0.5:
                        solution[i] += change
                    else:
                        solution[i] -= change

                    if solution[i] < 0:
                        solution[i] = 0
                    if solution[i] > 1:
                        solution[i] = 1
            else:
                solution[i] = np.random.rand()

        solutionScores.append(checkSolution(solution))

    bestSolutionIdx = solutionScores.index(min(solutionScores))
    worstSolutionIdx = solutionScores.index(max(solutionScores))

    if iter % display == 0:
        print('Iteration ', iter)
        print('Worst ', worstSolutionIdx, solutionScores[worstSolutionIdx])
        print('Best ', bestSolutionIdx, solutionScores[bestSolutionIdx])
        print('Mean ', np.mean(solutionScores))

        losses.append(solutionScores[bestSolutionIdx])
        # draw best solution
        plt.cla()
        plt.axis([0, mapX + 1, 0, mapY + 1])

        drawSolution(harmonyMemory[bestSolutionIdx])

        plt.savefig('images/iter_' + str(iter) + '.png')

        plt.pause(0.1)

    harmonyMemory[worstSolutionIdx] = harmonyMemory[bestSolutionIdx][:]

plt.show()

plt.cla()
plt.plot(losses)
plt.savefig('loss.png')

