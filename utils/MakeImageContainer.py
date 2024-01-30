from PyQt6.QtWidgets import QLabel, QSizePolicy
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
import cv2
import numpy as np


class MakeImageContainer(QLabel):

    def __init__(self, image_path="",
                 x=10, y=10,
                 w=512, h=512):
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.data_image = []
        self.selected_image = None
        self.display_image = []
        self.display_image_w = w
        self.display_image_h = h
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        #self.setFixedHeight(h)
        #self.setFixedWidth(w)
        self.setStyleSheet("background-color:#dddddd;\
                            border: 0px solid #0000dd;\
                           padding: 0px;")
        self.update_image(image_path)

    def update_image(self, image_path, processed=False):
        self.selected_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if not processed:
            self.display_image = cv2.resize(self.selected_image, (self.display_image_w, self.display_image_h),
                                            interpolation=cv2.INTER_NEAREST)
            print("Un-Processed Image Shape: " + str(self.display_image.shape))
        if processed:
            self.display_image = self.selected_image
            print("Processed Image Shape: "+str(self.display_image.shape))

        self.display_image_h, self.display_image_w = self.display_image.shape
        disp_im_byt_per_ln = self.display_image_w
        q_image = QImage(self.display_image, self.display_image_w,
                         self.display_image_h, disp_im_byt_per_ln,
                         QImage.Format.Format_Grayscale8)
        pixel_map = QPixmap.fromImage(q_image)
        self.setPixmap(pixel_map)

    def get_data_image(self):
        self.data_image = np.asarray(self.display_image)
        self.data_image = self.data_image/255
        return self.data_image
