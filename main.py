from sense_hat import SenseHat
import random
import time
sense = SenseHat()

black = [0, 0, 0]  # Red
red = [255, 0, 0]  # Red

def getTotalActiveAdjacentCells(inputGrid, targetCell):
    totalActiveAdjacentCells = 0

grid = []

for currentIndex in range(0, 8):
    currentRow = []
    for currentIndex in range(0, 8):
        if random.randint(0, 1):
            currentRow.append(red)
        else:
            currentRow.append(black)
    grid.append(currentRow)

for currentInteration in range(0, 100):
    time.sleep(1)


displayGrid = [currentCell for currentSublist in grid for currentCell in currentSublist]
sense.set_pixels(displayGrid)