# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PySide6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(328, 339)
        MainWindow.setStyleSheet("QFrame {\n"
"background:black;\n"
"color:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 331, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(25, 0, 291, 31))
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 321, 31))
        self.label_2.setStyleSheet("font-size: 20px;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 301, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.connection_status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.connection_status.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.connection_status.setObjectName("connection_status")
        self.gridLayout.addWidget(self.connection_status, 0, 1, 1, 1)
        self.team_file_directory = QtWidgets.QLabel(self.gridLayoutWidget)
        self.team_file_directory.setObjectName("team_file_directory")
        self.gridLayout.addWidget(self.team_file_directory, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.destination_file_directory = QtWidgets.QLabel(self.gridLayoutWidget)
        self.destination_file_directory.setObjectName("destination_file_directory")
        self.gridLayout.addWidget(self.destination_file_directory, 3, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.results_file_directory = QtWidgets.QLabel(self.gridLayoutWidget)
        self.results_file_directory.setWordWrap(True)
        self.results_file_directory.setObjectName("results_file_directory")
        self.gridLayout.addWidget(self.results_file_directory, 1, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 240, 301, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.preq_json = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.preq_json.setObjectName("preq_json")
        self.gridLayout_2.addWidget(self.preq_json, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.preq_irsdk = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.preq_irsdk.setObjectName("preq_irsdk")
        self.gridLayout_2.addWidget(self.preq_irsdk, 2, 0, 1, 1)
        self.full_json = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.full_json.setObjectName("full_json")
        self.gridLayout_2.addWidget(self.full_json, 1, 1, 1, 1)
        self.full_irsdk = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.full_irsdk.setObjectName("full_irsdk")
        self.gridLayout_2.addWidget(self.full_irsdk, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Pug\'s iRacing Results Reader</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Read results via IRSDK/.json file.</span></p></body></html>"))
        self.connection_status.setText(_translate("MainWindow", "False"))
        self.team_file_directory.setText(_translate("MainWindow", "None"))
        self.label_3.setText(_translate("MainWindow", "iRacing Connection Status: "))
        self.pushButton.setText(_translate("MainWindow", "Select Custom Team File"))
        self.pushButton_2.setText(_translate("MainWindow", "Select Destination File"))
        self.destination_file_directory.setText(_translate("MainWindow", "results.csv"))
        self.pushButton_3.setText(_translate("MainWindow", "Select Results File"))
        self.results_file_directory.setText(_translate("MainWindow", "None"))
        self.preq_json.setText(_translate("MainWindow", "JSON"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Pre-Qualifying Version:</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Full Version:</span><br/></p></body></html>"))
        self.preq_irsdk.setText(_translate("MainWindow", "IRSDK"))
        self.full_json.setText(_translate("MainWindow", "JSON"))
        self.full_irsdk.setText(_translate("MainWindow", "IRSDK"))
