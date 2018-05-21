# run this under the root folder of the project
# ffmpeg -framerate 25 -i images/iter_%d.png -c:v libx264 -pix_fmt yuv420p out.mp4
# ffmpeg -i out.mp4 out.gif

import numpy as np
import matplotlib.pyplot as plt


class Gym:
    def __init__(self, mapX, mapY, startPos, destPos, step, color):
        self.mapX = mapX
        self.mapY = mapY
        self.startPos = startPos
        self.destPos = destPos
        self.step = step

        self.color = color

        self.plt = plt


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


    def drawSolution(self, solution, iter):
        color = self.color
        newPosition = self.startPos[:]
        lastPosition = self.startPos[:]

        self.plt.cla()
        self.plt.axis([0, self.mapX + 1, 0, self.mapY + 1])

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

            self.plt.plot(x, y, c=color)

            lastPosition = newPosition[:]

        self.plt.text(90, 10, iter)
        self.plt.savefig('images/iter_' + str(iter) + '.png')
