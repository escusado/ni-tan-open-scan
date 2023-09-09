import math
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.load_default()
rowHeight = 8
verticalPadding = 2


class MenuScreen:
    def __init__(self, menu):
        # Menu screen size
        self.screenWidth = 128
        self.screenHeight = 32

        # Menu state
        self.rowsToShow = 4
        self.currentPath = []
        self.currentSelectedRow = 0
        self.currentMenuRotaryPosition = 0
        self.menuHeight = ((rowHeight*(len(menu))) +
                           (verticalPadding*2)+1) - (rowHeight*2)
        self.menu = menu

        print('Menu created')

    def updateRotaryPosition(self, delta):
        self.currentMenuRotaryPosition += delta
        if self.currentMenuRotaryPosition > self.menuHeight:
            self.currentMenuRotaryPosition = self.menuHeight
        if self.currentMenuRotaryPosition < 0:
            self.currentMenuRotaryPosition = 0

    def getScreen(self):
        return self.getMenuSelectionAt(self.currentMenuRotaryPosition)

    def handleSwitchPressAndNavigate(self, isEncoderPressed):
        print('MenuScreen handleSwitchPress')
        if isEncoderPressed:
            return self.menu[self.currentSelectedRow]['label']

    def getMenuSelectionAt(self, y=0):
        imageHeight = (rowHeight*(len(self.menu)))+(verticalPadding*2)+1

        # allow for selection to work w/out scrolling
        self.currentSelectedRow = math.ceil(y/rowHeight)
        if self.currentSelectedRow > len(self.menu)-1:
            self.currentSelectedRow = len(self.menu)-1

        # prevet overflow render
        y = y if y < imageHeight-self.screenHeight else imageHeight-self.screenHeight
        y = y if y > -1 else 0
        image = Image.new("1", (self.screenWidth, imageHeight))
        draw = ImageDraw.Draw(image)
        draw.rectangle(
            (0, 0, self.screenWidth, self.screenHeight), outline=0, fill=0)
        x = 0

        # iterate over menu items
        for idx, row in enumerate(self.menu):
            isCurrentRow = '> ' if idx == self.currentSelectedRow else '  '
            draw.text((x, verticalPadding+(rowHeight * idx)), isCurrentRow+row['label'].capitalize(
            ), font=font, fill=255)

        return image.crop((0, y, self.screenWidth, y + self.screenHeight))
