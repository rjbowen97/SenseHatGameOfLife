from sense_hat import SenseHat
import random
import time


class SenseHatGOL:
    def __init__(self, secondsPerIteration, iterationLimit):
        self.secondsPerIteration = secondsPerIteration
        self.iterationLimit = iterationLimit
        self.initSenseHat()
        self.golGrid = GOLGrid()

    def initSenseHat(self):
        self.sense = SenseHat()
        self.sense.low_light = True

    def execute(self):
        currentIteration = 0
        while True:
            time.sleep(self.secondsPerIteration)

            displayGrid = [
                currentCell for currentSublist in self.golGrid.grid for currentCell in currentSublist]
            self.sense.set_pixels(displayGrid)
            currentIteration += 1


class GOLGrid:
    def __init__(self):
        self.initGrid()

    def initGrid(self):
        self.grid = []

        for currentRowIndex in range(0, 8):
            currentRow = []
            for currentColumnIndex in range(0, 8):
                currentRow.append(False)
            self.grid.append(currentRow)

    def stepGridForward(self):
        bufferGrid = []
        for currentRowIndex in range(0, 8):
            currentBufferRow = []
            for currentColumnIndex in range(0, 8):
                totalActiveAdjacentCells = self.getTotalLivingNeighborsOfTargetCell(
                    currentRowIndex, currentColumnIndex)

                if self.grid[currentRowIndex][currentColumnIndex] == False:
                    if totalActiveAdjacentCells == 3:
                        currentBufferRow.append(True)
                    else:
                        currentBufferRow.append(False)
                else:
                    if totalActiveAdjacentCells < 2 or totalActiveAdjacentCells > 3:
                        currentBufferRow.append(False)
                    else:
                        currentBufferRow.append(True)
            bufferGrid.append(currentBufferRow)
        self.grid = bufferGrid

    def getTotalLivingNeighborsOfTargetCell(self, targetCellRow, targetCellColumn):
        totalLivingNeighbors = 0

        if self.grid[(targetCellRow - 1) % 8][(targetCellColumn - 1) % 8]:
            totalLivingNeighbors += 1

        if self.grid[(targetCellRow - 1) % 8][(targetCellColumn) % 8]:
            totalLivingNeighbors += 1

        if self.grid[(targetCellRow - 1) % 8][(targetCellColumn + 1) % 8]:
            totalLivingNeighbors += 1

        if self.grid[(targetCellRow + 1) % 8][(targetCellColumn - 1) % 8]:
            totalLivingNeighbors += 1

        if self.grid[(targetCellRow + 1) % 8][(targetCellColumn) % 8]:
            totalLivingNeighbors += 1

        if self.grid[(targetCellRow + 1) % 8][(targetCellColumn + 1) % 8]:
            totalLivingNeighbors += 1

        if self.grid[(targetCellRow) % 8][(targetCellColumn - 1) % 8]:
            totalLivingNeighbors += 1

        if self.grid[(targetCellRow) % 8][(targetCellColumn + 1) % 8]:
            totalLivingNeighbors += 1

        return totalLivingNeighbors