from sense_hat import SenseHat

sense = SenseHat()

black = [0, 0, 0]  # Red
red = [255, 0, 0]  # Red



question_mark = [
black, black, black, red, red, black, black, black,
black, black, red, black, black, red, black, black,
black, black, black, black, black, red, black, black,
black, black, black, black, red, black, black, black,
black, black, black, red, black, black, black, black,
black, black, black, red, black, black, black, black,
black, black, black, black, black, black, black, black,
black, black, black, red, black, black, black, black
]




sense.set_pixels(question_mark)

# sense.clear()