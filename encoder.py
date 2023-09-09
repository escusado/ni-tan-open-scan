
import board
from rainbowio import colorwheel
from adafruit_seesaw import seesaw, neopixel, rotaryio, digitalio


# For use with the STEMMA connector on QT Py RP2040
# import busio
# i2c = busio.I2C(board.SCL1, board.SDA1)
# seesaw = seesaw.Seesaw(i2c, 0x36)

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
seesaw = seesaw.Seesaw(i2c, 0x36)

encoder = rotaryio.IncrementalEncoder(seesaw)
seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
switch = digitalio.DigitalIO(seesaw, 24)

pixel = neopixel.NeoPixel(seesaw, 6, 1)
pixel.brightness = 0.5


class Encoder:
    def __init__(self):
        self.last_position = -1
        self.color = 0  # start at red
        self.changeDelta = 0

    def getEncoderPosition(self):
        position = -encoder.position

        if position != self.last_position:
            # Change the LED color.
            if position > self.last_position:  # Advance forward through the colorwheel.
                self.color += 10
            else:
                self.color -= 10  # Advance backward through the colorwheel.
            self.color = (self.color + 256) % 256  # wrap around to 0-256
            pixel.fill(colorwheel(self.color))

        self.changeDelta = self.last_position - position

        self.last_position = position
        return position

    def getEncoderDelta(self):
        self.getEncoderPosition()
        return self.changeDelta

    def isEncoderPressed(self):
        return switch.value == False
