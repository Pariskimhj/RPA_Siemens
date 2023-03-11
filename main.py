from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow, QMessageBox)
from ui_main import Ui_MainWindow
import sys
from sap import SapGui

# Main project title
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Automation SAP system")

        # SYSTEM PAGES / 버튼 누르면 해당 page 나오게
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_sap.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sap))
        self.btn_contacts.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contacts))
        self.btn_about.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_about))

        self.btn_open.clicked.connect(self.open_file) # open 버튼 클릭하면 파일 오픈

        #################################################
        # LOGIN INTO SAP SYSTEM
        self.btn_login.clicked.connect(self.login_sap)
        ##################################################

        self.btn_AssetList.clicked.connect(self.Asset_list)
        
    # 파일 열기
    def open_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Select spreadsheet")
        self.txt_file.setText(str(self.file[0]))
    
    def login_sap(self):
        self.sap = SapGui()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("login")
        msg.setText("Login Successfully")
        msg.exec()

    def Asset_list(self):
        # msgBox = QMessageBox()
        # msgBox.setWindowTitle('Asset list update')
        # msgBox.setIcon(QMessageBox.Question)
        # msgBox.setInformativeText('Are you sure you want to download updated asset list?')
        # msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # ret = msgBox.exec()

        # if ret == QMessageBox.Yes:
        self.sap.Asset_list()
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.information)
        msgBox.setWindowTitle('Asset list update')
        msgBox.setText('Asset list Update completed.')
        msgBox.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
