from sense_hat import SenseHat
import random
import time
sense = SenseHat()

black = [0, 0, 0]  # Red
off = black

red = [255, 0, 0]  # Red
on = red

grid = []

for currentRowIndex in range(0, 8):
    currentRow = []
    for currentColumnIndex in range(0, 8):
        if random.randint(0, 1):
            currentRow.append(on)
        else:
            currentRow.append(black)
    grid.append(currentRow)

for currentInteration in range(0, 100):
    time.sleep(1)

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

            print(totalActiveAdjacentCells)
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

    grid = bufferGrid

    displayGrid = [
        currentCell for currentSublist in grid for currentCell in currentSublist]
    sense.set_pixels(displayGrid)
