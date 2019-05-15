from sense_hat import SenseHat
import random
import time
sense = SenseHat()

sense.low_light = True


black = [0, 0, 0]
off = black

red = [255, 0, 0]
green = [0, 255, 0]
yellow = [255, 255, 0]
on = yellow


def initGrid():
    grid = []

    for currentRowIndex in range(0, 8):
        currentRow = []
        for currentColumnIndex in range(0, 8):
            if random.randint(0, 1):
                currentRow.append(on)
            else:
                currentRow.append(black)
        grid.append(currentRow)
    return grid


grid = initGrid()

currentIteration = 0
while True:
    if currentIteration == 100:
        sense.set_pixel(0, 0, red)
        grid = initGrid()
        currentIteration = 0
    time.sleep(0.10)

    bufferGrid = []
    for currentRowIndex in range(0, 8):

        currentBufferRow = []
        for currentColumnIndex in range(0, 8):
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

    grid = bufferGrid

    displayGrid = [
        currentCell for currentSublist in grid for currentCell in currentSublist]
    sense.set_pixels(displayGrid)
    currentIteration += 1
