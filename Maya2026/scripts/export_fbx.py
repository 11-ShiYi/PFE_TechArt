import maya.cmds as cmds
import maya.mel as mel
import os
import utils


from PySide6 import QtWidgets, QtUiTools, QtCore
from PySide6.QtWidgets import QFileDialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Export FBX Tool")
        loader = QtUiTools.QUiLoader()

        self.base_dir = utils.get_root_dir()
        ui_path = os.path.join(self.base_dir, "scripts", "export_fbx_ui.ui")
        ui_file = QtCore.QFile(ui_path)
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)

        ui_file.close()

        self.setCentralWidget(self.ui)

        self.ui.browseButton.clicked.connect(self.browse_folder)
        self.ui.exportButton.clicked.connect(self.export_fbx)


    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open Folder")
        if folder_path:
            self.ui.pathEdit.setText(folder_path)

    def export_fbx(self):
        mel_settings_path = os.path.join(self.base_dir, "scripts", "fbx_settings.mel")
        mel.eval('source "{}";'.format(mel_settings_path.replace('\\', '/')))
        folder_path = self.ui.pathEdit.text()
        
        if os.path.exists(folder_path):
            mesh_list = cmds.ls(sl = 1)
            for mesh in mesh_list:
                cmds.select(cl = 1)
                cmds.select(mesh)

                # delete "|" in case a scene has two objects with the same name
                mesh_name = mesh.split("|")[-1]

                full_path = os.path.join(folder_path, mesh_name + '.fbx').replace('\\', '/')
                mel.eval('FBXExport -f "{}" -s;'.format(full_path))
                print("Exported FBX to:", full_path)
        else:
            print("Folder path doesn't exist.")
        

_my_window_instance = None

def main():
    global _my_window_instance

    if _my_window_instance is not None:
        try:
            _my_window_instance.close()
            _my_window_instance.deleteLater()
        except:
            pass
        _my_window_instance = None

    _my_window_instance = MainWindow()
    _my_window_instance.show()
    _my_window_instance.raise_()
    _my_window_instance.activateWindow()


