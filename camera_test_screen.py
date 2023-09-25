from PIL import Image, ImageDraw, ImageFont
from camera_driver import Camera
from menu_screen import MenuScreen
camera = Camera()

font = ImageFont.load_default()

cameraTestMenuScreen = MenuScreen([
    {"label": "capture"},
    {"label": "back"}
])


class CameraTestScreen:
    def __init__(self):
        # Menu screen size
        self.screenWidth = 128
        self.screenHeight = 32

        self.encoderRotation = 0

    def updateRotaryPosition(self, delta):
        cameraTestMenuScreen.updateRotaryPosition(delta)
        self.encoderRotation += delta

    def handleSwitchPressAndNavigate(self, isEncoderPressed):
        selectedOption = cameraTestMenuScreen.handleSwitchPressAndNavigate(
            isEncoderPressed)

        if (selectedOption == 'capture'):
            camera.captureImage()
        elif (selectedOption == 'back'):
            return 'home'

    def getScreen(self):
        image = Image.new("1", (self.screenWidth, self.screenHeight))
        ImageDraw.Draw(image)
        image.paste(cameraTestMenuScreen.getScreen())
        # draw.rectangle(
        #     (0, 0, self.screenWidth, self.screenHeight), outline=0, fill=0)

        # draw.text((0, 0), self.axis+': ' +
        #           str(self.encoderRotation), font=font, fill=255)

        return image
