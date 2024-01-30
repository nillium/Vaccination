import cv2
import numpy as np

from utils import MakeLabel, MakeMainWindow, MakeButton, MakeImageContainer, ImageSelector
import BuildModel
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
import sys
from Configuration import *

app = QApplication(sys.argv)
screen = app.primaryScreen()
screen_geometry = screen.geometry()
screen_w = screen_geometry.width()
screen_h = screen_geometry.height()

app_x = round((screen_w - app_w) / 2)
app_y = round((screen_h - app_h) / 2)
MainWindow = MakeMainWindow.MainWindow(x=app_x, y=app_y, w=app_w, h=app_h, title="FMI - ML Dev Tool")

def load_custom_input():
    custom_image_path = ImageSelector.select_image()
    image_one.update_image(custom_image_path)
    selected_input = cv2.imread(custom_image_path, cv2.IMREAD_GRAYSCALE)
    selected_input_array = np.asarray(selected_input)
    selected_input_array = selected_input_array.reshape((1, sample_h, sample_w, 1))

    output = model.predict(selected_input_array)
    print('Prediction' + str(output))
    if output[0] <= 0.2:
        output_info.setText("NOISE")
    elif output[0] > 0.2:
        output_info.setText("SIGNAL")

def load_custom_filter():

    filters = np.zeros((filter_size, filter_size, 1, number_of_filters))
    for s in range(0, number_of_filters):
        custom_filter_input_image = cv2.imread('data/custom_filter_input_%d.png' % s, cv2.IMREAD_GRAYSCALE)
        cv2.imshow('custom filter input image', custom_filter_input_image)
        cv2.waitKey(500)
        (w, h) = custom_filter_input_image.shape
        print('****** FILTER INPUT IMAGE PROPS ******')
        print('Custom Filter Input Image %d Width: ' % s + str(w))
        print('Custom Filter Input Image %d Height: ' % s + str(h))
        custom_filter_image = cv2.resize(custom_filter_input_image, (filter_size, filter_size), interpolation=cv2.INTER_LINEAR)

        current_filter = np.zeros((filter_size, filter_size))
        print('****** CUSTOM FILTER PROPS******')
        print('Custom Filter Shape: ' + str(current_filter.shape))
        custom_filter_array = np.asarray(custom_filter_image)
        for i in range(0, filter_size):
            for j in range(0, filter_size):
                if 192 < custom_filter_array[i, j] <= 255:
                    current_filter[i, j] = 1
                elif 64 < custom_filter_array[i, j] <= 192:
                    current_filter[i, j] = 0
                elif 0 <= custom_filter_array[i, j] <= 64:
                    current_filter[i, j] = -1
        # print(current_filter)
        print('******')
        # print('custom_filter_%d.png' % s)
        cv2.imshow('current filter', current_filter)
        cv2.waitKey(500)
        filters[:, :, 0, s] = current_filter
        cv2.imwrite('custom_filter_%d.png' % s, current_filter)
        print(s)
    #print(filters.shape)
    np.save("data/custom_filter.npy", filters)
load_custom_filter()

# LAYOUTS
root_layout = QHBoxLayout()

pane_one = QVBoxLayout()  # Input
pane_two = QVBoxLayout()  # Convolve
pane_three = QVBoxLayout()  # Convolve Output

# BUTTONS
load_custom_input_btn = MakeButton.MakeButton("Load Custom Input", call_on_press=load_custom_input, w=sample_w)

# LABELS
one_lbl = MakeLabel.MakeLabel(w=sample_w, h=20, align="c", label_text="INPUT", size_policy="fixed")
two_lbl = MakeLabel.MakeLabel(w=sample_w, h=20, align="c", label_text="FILTER", size_policy="fixed")
output_info = MakeLabel.MakeLabel(w=sample_w, h=20, align="c", label_text="OUTPUT", size_policy="fixed")

# IMAGES
image_one = MakeImageContainer.MakeImageContainer(w=sample_w, h=sample_h, image_path="checker.png")
#image_two = MakeImageContainer.MakeImageContainer(w=256, h=256, image_path="checker.png")

# root_layout.addLayout(root_top)
root_layout.addLayout(pane_one)
root_layout.addLayout(pane_two)
root_layout.addLayout(pane_three)

# ONE
pane_one.addWidget(one_lbl)
pane_one.addWidget(image_one)
pane_one.addWidget(load_custom_input_btn)
pane_one.setAlignment(Qt.AlignmentFlag.AlignTop)

pane_two.addWidget(output_info)

model = BuildModel.build_model()

if __name__ == '__main__':
    MainWindow.setLayout(root_layout)
    MainWindow.show()
    sys.exit(app.exec())
