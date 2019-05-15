from sense_hat import SenseHat
import random
import time

sense = SenseHat()
sense.low_light = True

secondsPerIteration = 1
iterationLimit = 1000

off = [0, 0, 0]
on = [255, 255, 0]


def initGrid():
    grid = []

    for currentRowIndex in range(0, 8):
        currentRow = []
        for currentColumnIndex in range(0, 8):
            if random.randint(0, 1):
                currentRow.append(on)
            else:
                currentRow.append(off)
        grid.append(currentRow)
    return grid


def getAdjacentCellTotal(grid):
    totalActiveAdjacentCells = 0

    if currentRowIndex - 1 >= 0:
        if currentColumnIndex - 1 >= 0:
            if grid[currentRowIndex - 1][currentColumnIndex - 1] == on:
                totalActiveAdjacentCells += 1

        if grid[currentRowIndex - 1][currentColumnIndex] == on:
            totalActiveAdjacentCells += 1

        if currentColumnIndex + 1 <= 7:
            if grid[currentRowIndex - 1][currentColumnIndex + 1] == on:
                totalActiveAdjacentCells += 1

    if currentRowIndex + 1 <= 7:
        if currentColumnIndex - 1 >= 0:
            if grid[currentRowIndex + 1][currentColumnIndex - 1] == on:
                totalActiveAdjacentCells += 1

        if grid[currentRowIndex + 1][currentColumnIndex] == on:
            totalActiveAdjacentCells += 1

        if currentColumnIndex + 1 <= 7:
            if grid[currentRowIndex + 1][currentColumnIndex + 1] == on:
                totalActiveAdjacentCells += 1

    if currentColumnIndex - 1 >= 0:
        if grid[currentRowIndex][currentColumnIndex - 1] == on:
            totalActiveAdjacentCells += 1
    if currentColumnIndex + 1 <= 7:
        if grid[currentRowIndex][currentColumnIndex + 1] == on:
            totalActiveAdjacentCells += 1


currentIteration = 0

grid = initGrid()
while True:
    time.sleep(secondsPerIteration)

    bufferGrid = []
    for currentRowIndex in range(0, 8):

        currentBufferRow = []
        for currentColumnIndex in range(0, 8):
            totalActiveAdjacentCells = getAdjacentCellTotal(grid)

            if grid[currentRowIndex][currentColumnIndex] == off:
                if totalActiveAdjacentCells == 3:
                    currentBufferRow.append(on)
                else:
                    currentBufferRow.append(off)
            else:
                if totalActiveAdjacentCells < 2 or totalActiveAdjacentCells > 3:
                    currentBufferRow.append(off)
                else:
                    currentBufferRow.append(on)
        bufferGrid.append(currentBufferRow)

    if grid == bufferGrid or currentIteration == iterationLimit:
        bufferGrid = initGrid()
        on[0] = random.randint(0, 255)
        on[1] = random.randint(0, 255)
        on[2] = random.randint(0, 255)
        currentIteration = 0

    grid = bufferGrid

    displayGrid = [
        currentCell for currentSublist in grid for currentCell in currentSublist]
    sense.set_pixels(displayGrid)
    currentIteration += 1
