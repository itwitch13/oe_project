# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(907, 448)
        MainWindow.setMinimumSize(QtCore.QSize(970, 410))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 7, 950, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.appHorizontalLayout = QtWidgets.QHBoxLayout()
        self.appHorizontalLayout.setObjectName("appHorizontalLayout")
        self.graphWidget = PlotWidget(self.verticalLayoutWidget)
        self.graphWidget.setMinimumSize(QtCore.QSize(250, 150))
        self.graphWidget.setObjectName("graphWidget")
        self.appHorizontalLayout.addWidget(self.graphWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.parametersHorizontalLayout = QtWidgets.QHBoxLayout()
        self.parametersHorizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.parametersHorizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.parametersHorizontalLayout.setObjectName("parametersHorizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(550, 380))
        self.tabWidget.setObjectName("tabWidget")
        self.graphTab = QtWidgets.QWidget()
        self.graphTab.setObjectName("graphTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.graphTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.graphTab)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.iterationLineEdit = QtWidgets.QLineEdit(self.graphTab)
        self.iterationLineEdit.setObjectName("iterationLineEdit")
        self.verticalLayout_6.addWidget(self.iterationLineEdit)
        self.label_4 = QtWidgets.QLabel(self.graphTab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.graphValPushButton = QtWidgets.QPushButton(self.graphTab)
        self.graphValPushButton.setObjectName("graphValPushButton")
        self.verticalLayout_6.addWidget(self.graphValPushButton)
        self.graphAverPushButton = QtWidgets.QPushButton(self.graphTab)
        self.graphAverPushButton.setObjectName("graphAverPushButton")
        self.verticalLayout_6.addWidget(self.graphAverPushButton)
        self.stdDevPushButton = QtWidgets.QPushButton(self.graphTab)
        self.stdDevPushButton.setObjectName("stdDevPushButton")
        self.verticalLayout_6.addWidget(self.stdDevPushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.graphTab, "")
        self.configurationTab = QtWidgets.QWidget()
        self.configurationTab.setObjectName("configurationTab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.configurationTab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(6, 10, 511, 351))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.selectionComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectionComboBox.sizePolicy().hasHeightForWidth())
        self.selectionComboBox.setSizePolicy(sizePolicy)
        self.selectionComboBox.setObjectName("selectionComboBox")
        self.verticalLayout_3.addWidget(self.selectionComboBox)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.crossoverComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crossoverComboBox.sizePolicy().hasHeightForWidth())
        self.crossoverComboBox.setSizePolicy(sizePolicy)
        self.crossoverComboBox.setObjectName("crossoverComboBox")
        self.verticalLayout_3.addWidget(self.crossoverComboBox)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.mutationComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mutationComboBox.sizePolicy().hasHeightForWidth())
        self.mutationComboBox.setSizePolicy(sizePolicy)
        self.mutationComboBox.setObjectName("mutationComboBox")
        self.verticalLayout_3.addWidget(self.mutationComboBox)
        self.iteratePushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iteratePushButton.sizePolicy().hasHeightForWidth())
        self.iteratePushButton.setSizePolicy(sizePolicy)
        self.iteratePushButton.setObjectName("iteratePushButton")
        self.verticalLayout_3.addWidget(self.iteratePushButton)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(-1, 30, -1, 6)
        self.formLayout.setObjectName("formLayout")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.savePushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.savePushButton.setObjectName("savePushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.savePushButton)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.timeLcdNumber = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.timeLcdNumber.setObjectName("timeLcdNumber")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.timeLcdNumber)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)
        self.percentLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percentLineEdit.sizePolicy().hasHeightForWidth())
        self.percentLineEdit.setSizePolicy(sizePolicy)
        self.percentLineEdit.setObjectName("percentLineEdit")
        self.verticalLayout_8.addWidget(self.percentLineEdit)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.tournamentLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tournamentLineEdit.sizePolicy().hasHeightForWidth())
        self.tournamentLineEdit.setSizePolicy(sizePolicy)
        self.tournamentLineEdit.setObjectName("tournamentLineEdit")
        self.verticalLayout_8.addWidget(self.tournamentLineEdit)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.eliteLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eliteLineEdit.sizePolicy().hasHeightForWidth())
        self.eliteLineEdit.setSizePolicy(sizePolicy)
        self.eliteLineEdit.setObjectName("eliteLineEdit")
        self.verticalLayout_8.addWidget(self.eliteLineEdit)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.crossProbLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crossProbLineEdit.sizePolicy().hasHeightForWidth())
        self.crossProbLineEdit.setSizePolicy(sizePolicy)
        self.crossProbLineEdit.setObjectName("crossProbLineEdit")
        self.verticalLayout_8.addWidget(self.crossProbLineEdit)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_8.addWidget(self.label_18)
        self.coefLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.coefLineEdit.setObjectName("coefLineEdit")
        self.verticalLayout_8.addWidget(self.coefLineEdit)
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_8.addWidget(self.label_17)
        self.realValueComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.realValueComboBox.sizePolicy().hasHeightForWidth())
        self.realValueComboBox.setSizePolicy(sizePolicy)
        self.realValueComboBox.setObjectName("realValueComboBox")
        self.verticalLayout_8.addWidget(self.realValueComboBox)
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_8.addWidget(self.label_19)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(-1, -1, 27, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.populationLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.populationLineEdit.sizePolicy().hasHeightForWidth())
        self.populationLineEdit.setSizePolicy(sizePolicy)
        self.populationLineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.populationLineEdit.setObjectName("populationLineEdit")
        self.verticalLayout_4.addWidget(self.populationLineEdit)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.generationLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generationLineEdit.sizePolicy().hasHeightForWidth())
        self.generationLineEdit.setSizePolicy(sizePolicy)
        self.generationLineEdit.setObjectName("generationLineEdit")
        self.verticalLayout_4.addWidget(self.generationLineEdit)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.mutationLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mutationLineEdit.sizePolicy().hasHeightForWidth())
        self.mutationLineEdit.setSizePolicy(sizePolicy)
        self.mutationLineEdit.setObjectName("mutationLineEdit")
        self.verticalLayout_4.addWidget(self.mutationLineEdit)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.xboundLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xboundLineEdit.sizePolicy().hasHeightForWidth())
        self.xboundLineEdit.setSizePolicy(sizePolicy)
        self.xboundLineEdit.setObjectName("xboundLineEdit")
        self.verticalLayout_4.addWidget(self.xboundLineEdit)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.yboundLneEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yboundLneEdit.sizePolicy().hasHeightForWidth())
        self.yboundLneEdit.setSizePolicy(sizePolicy)
        self.yboundLneEdit.setObjectName("yboundLneEdit")
        self.verticalLayout_4.addWidget(self.yboundLneEdit)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.configurationTab, "")
        self.parametersHorizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.parametersHorizontalLayout)
        self.appHorizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.appHorizontalLayout)
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionGet_info = QtWidgets.QAction(MainWindow)
        self.actionGet_info.setObjectName("actionGet_info")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionGet_info)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_12.setText(_translate("MainWindow", "Iteration"))
        self.label_4.setText(_translate("MainWindow", "Generate plot by:"))
        self.graphValPushButton.setText(_translate("MainWindow", "Function values"))
        self.graphAverPushButton.setText(_translate("MainWindow", "Average value of the function"))
        self.stdDevPushButton.setText(_translate("MainWindow", "Standard deviation of the function"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphTab), _translate("MainWindow", "Graph"))
        self.label.setText(_translate("MainWindow", "Selection"))
        self.label_2.setText(_translate("MainWindow", "Crossover"))
        self.label_3.setText(_translate("MainWindow", "Mutate"))
        self.label_10.setText(_translate("MainWindow", "Time"))
        self.savePushButton.setText(_translate("MainWindow", "Save"))
        self.label_11.setText(_translate("MainWindow", "Configuration"))
        self.label_16.setText(_translate("MainWindow", "Percentage selection"))
        self.label_15.setText(_translate("MainWindow", "Size of tournament"))
        self.label_14.setText(_translate("MainWindow", "Elite stratrgy - amount"))
        self.label_13.setText(_translate("MainWindow", "Crossover probability"))
        self.label_17.setText(_translate("MainWindow", "Is in real value"))
        self.label_18.setText(_translate("MainWindow", "Coefficient"))
        self.label_9.setText(_translate("MainWindow", "Population size"))
        self.label_8.setText(_translate("MainWindow", "Generations"))
        self.label_7.setText(_translate("MainWindow", "Mutation rate"))
        self.label_6.setText(_translate("MainWindow", "x boundaries"))
        self.label_5.setText(_translate("MainWindow", "y boundaries"))
        self.iteratePushButton.setText(_translate("MainWindow", "Run"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.configurationTab),
                                  _translate("MainWindow", "Configuration"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionGet_info.setText(_translate("MainWindow", "Get info"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))