# run this under the root folder of the project
# ffmpeg -framerate 25 -i solutions/iter_%d.png -c:v libx264 -pix_fmt yuv420p solutions.mp4
# ffmpeg -i solutions.mp4 solutions.gif
# ffmpeg -framerate 25 -i losses/loss_%d.png -c:v libx264 -pix_fmt yuv420p loss.mp4
# ffmpeg -i loss.mp4 loss.gif

import numpy as np
import matplotlib.pyplot as plt


class Gym:
    def __init__(self, mapX, mapY, startPos, destPos, step, color, iter):
        self.mapX = mapX
        self.mapY = mapY
        self.startPos = startPos
        self.destPos = destPos
        self.step = step
        self.iter = iter

        self.color = color

        self.losses = []

        self.solutionFigure = plt.figure()
        self.solutionPlot = self.solutionFigure.add_subplot(111)

        self.lossFigure = plt.figure()
        self.lossPlot = self.lossFigure.add_subplot(111)


    def checkSolution(self, solution):
        pos = self.startPos[:]

        for dir in solution:
            alpha = dir * 2 * np.pi

            pos[0] += self.step * np.cos(alpha)
            pos[1] += self.step * np.sin(alpha)

            if pos[0] < 0:
                pos[0] = 0
            if pos[1] < 0:
                pos[1] = 0
            if pos[0] > self.mapX:
                pos[0] = self.mapX
            if pos[1] > self.mapY:
                pos[1] = self.mapY

        loss = np.sqrt(np.square(self.destPos[1] - pos[1]) + np.square(self.destPos[0] - pos[0]))

        return loss


    def addLoss(self, iter, loss):
        self.losses.append(loss)

        self.lossPlot.cla()
        self.lossPlot.axis([0, self.iter + 1, 0, round(np.sqrt(self.mapX * self.mapX + self.mapY * self.mapY)) + 1])

        self.lossPlot.plot(self.losses, color='b')
        self.lossFigure.savefig('losses/loss_' + str(iter) + '.png')


    def drawSolution(self, iter, solution):
        color = self.color
        newPosition = self.startPos[:]
        lastPosition = self.startPos[:]

        self.solutionPlot.cla()
        self.solutionPlot.axis([0, self.mapX + 1, 0, self.mapY + 1])

        for dir in solution:
            alpha = dir * 2 * np.pi

            newPosition[0] += self.step * np.cos(alpha)
            newPosition[1] += self.step * np.sin(alpha)

            if newPosition[0] < 0:
                newPosition[0] = 0
            if newPosition[1] < 0:
                newPosition[1] = 0
            if newPosition[0] > self.mapX:
                newPosition[0] = self.mapX
            if newPosition[1] > self.mapY:
                newPosition[1] = self.mapY

            x = np.asarray([lastPosition[0], newPosition[0]])
            y = np.asarray([lastPosition[1], newPosition[1]])

            self.solutionPlot.plot(x, y, c=color)

            lastPosition = newPosition[:]

        self.solutionPlot.text(90, 10, iter)
        self.solutionFigure.savefig('solutions/iter_' + str(iter) + '.png')
