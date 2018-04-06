# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 458)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 451, 51))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(160, 20, 281, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 121, 23))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 100, 171, 161))
        self.graphicsView.setObjectName("graphicsView")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(190, 100, 271, 301))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(190, 80, 111, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 290, 131, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(70, 270, 54, 12))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 473, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuFiles = QtWidgets.QMenu(self.menuBar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuFiles.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Select image file"))
        self.pushButton.setText(_translate("MainWindow", "SelectFile"))
        self.label.setText(_translate("MainWindow", "image show"))
        self.label_2.setText(_translate("MainWindow", "Text in image"))
        self.pushButton_2.setText(_translate("MainWindow", "Pickup text"))
        self.label_3.setText(_translate("MainWindow", "》》》》"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
    #END

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow ):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.openfile)
        self.pushButton_2.clicked.connect(self.startpickup)
    
    def openfile(self):
        openFilesPath = "G:/temp/tf/ocr_image/"
        
        files, ok = QtWidgets.QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()",
                                                 openFilesPath,"All Files (*);;Image Files (*.jpg,*.png);;PDF Files (*.pdf)")
        if len(files):
            self.lineEdit.setText(", ".join(files))
        
        # #获取图像文件路径
        imagepath = self.lineEdit.text()
        
        # #在graphicsView中显示图像
        Png = QtGui.QPixmap(imagepath)  
        scene = QtWidgets.QGraphicsScene(self)
        scene.addPixmap(Png)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()
    
    def startpickup(self):
        # #获取图像文件路径
        imagefile = self.lineEdit.text()
        #self.textEdit.setText(str(text))
        
        # #对图像进行文字识别
        import ocr_image
        imgtext = ''
        
        try:
            imgtext = ocr_image.pickup_text_in_image(imagefile)
        except ():
            print('ocr have error...')
        # #把识别的文字 显示到文本框中
        self.textEdit.setText(str(imgtext))
    
    
if __name__=='__main__':
    
    app=QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    
    myW = MyWindow()
    
    myW.show()
    
    sys.exit(app.exec_())
