from PIL import Image, ImageDraw, ImageFont
font = ImageFont.load_default()


class StepperTestScreen:
    def __init__(self, axis):
        # Menu screen size
        self.screenWidth = 128
        self.screenHeight = 32

        self.axis = axis
        self.rotaryDelta = 0

    def updateRotaryPosition(self, delta):
        self.rotaryDelta += delta

    def handleSwitchPressAndNavigate(self, isEncoderPressed):
        if isEncoderPressed:
            return 'home'

    def getScreen(self):
        image = Image.new("1", (self.screenWidth, self.screenHeight))
        draw = ImageDraw.Draw(image)
        draw.rectangle(
            (0, 0, self.screenWidth, self.screenHeight), outline=0, fill=0)

        draw.text((0, 0), self.axis+': ' +
                  str(self.rotaryDelta), font=font, fill=255)

        return image
