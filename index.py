
from stepper_test_screen import StepperTestScreen
from menu_screen import MenuScreen
import time
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

from encoder_driver import Encoder
encoder = Encoder()

xAxisScreen = StepperTestScreen('X', 400)
yAxisScreen = StepperTestScreen('Y', 200)

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
font = ImageFont.load_default()

# Clear display.
disp.fill(0)
disp.show()
width = disp.width
height = disp.height
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
mainMenuScreen = MenuScreen([
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

screens = {
    "home": mainMenuScreen,
    "test x": xAxisScreen,
    "test y": yAxisScreen,
}
currentScreen = 'home'


while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    screens[currentScreen].updateRotaryPosition(encoder.getEncoderDelta())
    screenToNavigate = screens[currentScreen].handleSwitchPressAndNavigate(
        encoder.isEncoderPressed())

    # if scren in screens, set it to current
    if screenToNavigate in screens:
        currentScreen = screenToNavigate

    image.paste(screens[currentScreen].getScreen())

    disp.image(image)
    disp.show()
    time.sleep(0.1)
