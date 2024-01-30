from PyQt6.QtWidgets import QFileDialog
import os


def select_image():

    file_filter = 'Image File (*.png)'
    response = QFileDialog.getOpenFileName(
        caption='Select a file',
        directory=os.getcwd(),
        filter=file_filter,
        initialFilter='Image File (*.png)')
    file_dialog = QFileDialog()
    file_dialog.setWindowTitle('Open File')
    image_path = response[0]
    return image_path
