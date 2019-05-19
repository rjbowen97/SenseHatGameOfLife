from sense_hat import SenseHat
import random
import time


class SenseHatGOL:
    livingCellColor = [0, 0, 0]
    offColor = [0, 0, 0]

    def __init__(self, secondsPerIteration, iterationLimit):
        self.secondsPerIteration = secondsPerIteration
        self.iterationLimit = iterationLimit

        self.initSenseHat()
        self.initGOLGrid()

    def initSenseHat(self):
        self.sense = SenseHat()
        self.sense.low_light = False

    def initGOLGrid(self):
        self.golGrid = GOLGrid()
        self.golGrid.randomizeGrid()
        self.changelivingCellColor()

    def execute(self):
        currentIteration = 0
        while True:
            hasLivingCells = False
            displayGrid = []
            for currentSublist in self.golGrid.grid:
                for currentCell in currentSublist:
                    if currentCell:
                        displayGrid.append(self.livingCellColor)
                        hasLivingCells = True
                    else:
                        displayGrid.append(self.offColor)

            currentIteration += 1
            self.sense.set_pixels(displayGrid)

            if (currentIteration == self.iterationLimit or (not hasLivingCells) or self.golGrid.isStagnant):
                currentIteration = 0
                self.golGrid.randomizeGrid()
                self.changelivingCellColor()

            self.golGrid.stepGridForward()

            time.sleep(self.secondsPerIteration)


    def changelivingCellColor(self):
        self.livingCellColor[0] = random.randint(0, 255)
        self.livingCellColor[1] = random.randint(0, 255)
        self.livingCellColor[2] = random.randint(0, 255)


class GOLGrid:
    isStagnant = False

    def __init__(self):
        self.initGrid()

    def initGrid(self):

        self.grid = []

        for currentRowIndex in range(0, 8):
            currentRow = []
            for currentColumnIndex in range(0, 8):
                currentRow.append(False)
            self.grid.append(currentRow)

    def randomizeGrid(self):
        for currentRowIndex in range(0, len(self.grid)):
            for currentColumnIndex in range(0, len(self.grid[currentRowIndex])):
                self.grid[currentRowIndex][currentColumnIndex] = (
                    random.randint(0, 1) == 0)

    def stepGridForward(self):
        self.bufferGrid = []
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
            self.bufferGrid.append(currentBufferRow)

        self.isStagnant = (self.grid == self.bufferGrid)
        self.grid = self.bufferGrid

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


senseHatGOL = SenseHatGOL(0.5, 120)
senseHatGOL.execute()
