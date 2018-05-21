import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

import sys
sys.path.insert(0, '../')

from utils import Gym


gym = Gym(mapX = 100, mapY = 100, startPos = [0, 0], destPos = [100, 100], step = 2, color = 'r')

maxIter = 500

bandwidth = 0.01
solutionSize = 100
harmonyMemorySize = 30
harmonyMemoryConsiderationRate = 0.99
pitchAdjustRate = 0.01

harmonyMemory = np.random.random((harmonyMemorySize, solutionSize))

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

        solutionScores.append(gym.checkSolution(solution))

    bestSolutionIdx = solutionScores.index(min(solutionScores))
    worstSolutionIdx = solutionScores.index(max(solutionScores))

    harmonyMemory[worstSolutionIdx] = harmonyMemory[bestSolutionIdx][:]

    print('Iteration ', iter)
    print('Best ', bestSolutionIdx, solutionScores[bestSolutionIdx])

    losses.append(solutionScores[bestSolutionIdx])
    # draw best solution
    gym.drawSolution(harmonyMemory[bestSolutionIdx], iter)

plt.cla()
plt.plot(losses)
plt.savefig('loss.png')
