# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

from PIL import Image, ImageDraw, ImageFont
from menu import Menu

font = ImageFont.load_default()

# Clear display.
width = 128
height = 32
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
bottom = height - padding
top = padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# example python nested map objects
menu = Menu([
            {"label": "home"},
            {"label": "test x"},
            {"label": "test y"},
            {"label": "test cam"},
            {"label": "settings"},
            {"label": "666"},
            {"label": "777"},
            {"label": "888"},
            {"label": "999"},
            ])

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# render menu using menu.getMenuAt and draw it on the image
image.paste(menu.getMenuAt(0), (0, 0))

image.show()
