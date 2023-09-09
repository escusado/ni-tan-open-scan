from PIL import Image, ImageDraw, ImageFont

font = ImageFont.load_default()
rowHeight = 8


class Menu:
    def __init__(self, menu):
        # Menu screen size
        self.width = 128
        self.height = 32

        # Menu state
        self.rowsToShow = 4
        self.currentPath = []
        self.currentSelectedRow = 2

        self.menu = menu

        print('Menu created')

    def getMenuAt(self, y=0):
        verticalPadding = 2
        imageHeight = (rowHeight*(len(self.menu)))+(verticalPadding*2)+1
        y = y if y < imageHeight else imageHeight
        y = y if y > -1 else 0
        image = Image.new("1", (self.width, imageHeight))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        x = 0

        # iterate over menu items
        for idx, row in enumerate(self.menu):
            isCurrentRow = '> ' if idx == self.currentSelectedRow else '  '
            draw.text((x, verticalPadding+(rowHeight * idx)), isCurrentRow+row['label'].capitalize(
            ), font=font, fill=255)

        print('image height: ', imageHeight)

        draw.rectangle((0, imageHeight-1, self.width,
                       imageHeight), outline=1, fill=255)

        return image.crop((0, y, self.width, y + self.height))
