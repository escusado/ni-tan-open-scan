from picamera2 import Picamera2
from libcamera import Transform, controls
import time
import os

os.environ["LIBCAMERA_LOG_LEVELS"] = "3"


class Camera:
    def __init__(self):
        print('initializing camera...')
        self.picam2 = Picamera2()

    def capturePreview(self):
        print('capturing preview')
        # self.picam2.stop()
        # self.picam2.configure(self.picam2.create_preview_configuration(
        #     transform=Transform(vflip=True)))
        # self.picam2.start()
        # self.picam2.autofocus_cycle(wait=True)
        # self.picam2.capture_file("preview.jpg")

    def captureImage(self):
        print('capturing image')

        self.picam2.stop()

        self.picam2.start()
        time.sleep(2)
        self.picam2.autofocus_cycle(wait=True)
        config = self.picam2.create_still_configuration(
            transform=Transform(vflip=True))
        self.picam2.switch_mode_and_capture_file(config, "capture.jpg")

        # picam2.capture_file("capture.jpg")

        print('captured!')
