# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyarchinit_images_directory_export_ui.ui'
#
# Created: Mon Oct 15 17:00:39 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_Dialog_img_exp(object):
    def setupUi(self, Dialog_img_exp):
        Dialog_img_exp.setObjectName(_fromUtf8("Dialog_img_exp"))
        Dialog_img_exp.setWindowModality(QtCore.Qt.NonModal)
        Dialog_img_exp.setEnabled(True)
        Dialog_img_exp.resize(588, 511)
        Dialog_img_exp.setMinimumSize(QtCore.QSize(450, 279))
        Dialog_img_exp.setMaximumSize(QtCore.QSize(1000, 1000))
        Dialog_img_exp.setCursor(QtCore.Qt.PointingHandCursor)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/directoryExp.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_img_exp.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog_img_exp)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(Dialog_img_exp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: rgb(216, 216, 216);"))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.formLayout = QtGui.QFormLayout(self.tab)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBox_tipo_reperto = QtGui.QCheckBox(self.tab)
        self.checkBox_tipo_reperto.setEnabled(False)
        self.checkBox_tipo_reperto.setObjectName(_fromUtf8("checkBox_tipo_reperto"))
        self.horizontalLayout.addWidget(self.checkBox_tipo_reperto)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.checkBox_fase = QtGui.QCheckBox(self.tab)
        self.checkBox_fase.setObjectName(_fromUtf8("checkBox_fase"))
        self.horizontalLayout_4.addWidget(self.checkBox_fase)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.checkBox_criterio_schedatura = QtGui.QCheckBox(self.tab)
        self.checkBox_criterio_schedatura.setEnabled(False)
        self.checkBox_criterio_schedatura.setObjectName(_fromUtf8("checkBox_criterio_schedatura"))
        self.horizontalLayout_3.addWidget(self.checkBox_criterio_schedatura)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.checkBox_definizione_materiale = QtGui.QCheckBox(self.tab)
        self.checkBox_definizione_materiale.setEnabled(False)
        self.checkBox_definizione_materiale.setObjectName(_fromUtf8("checkBox_definizione_materiale"))
        self.horizontalLayout_2.addWidget(self.checkBox_definizione_materiale)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 5)
        spacerItem5 = QtGui.QSpacerItem(170, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 6, 5, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(438, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 4, 2, 1, 4)
        self.checkBox_periodo = QtGui.QCheckBox(self.tab)
        self.checkBox_periodo.setObjectName(_fromUtf8("checkBox_periodo"))
        self.gridLayout.addWidget(self.checkBox_periodo, 1, 0, 1, 1)
        self.checkBox_US = QtGui.QCheckBox(self.tab)
        self.checkBox_US.setStyleSheet(_fromUtf8("selection-background-color: rgb(255, 255, 255);"))
        self.checkBox_US.setObjectName(_fromUtf8("checkBox_US"))
        self.gridLayout.addWidget(self.checkBox_US, 0, 0, 1, 4)
        self.checkBox_struttura = QtGui.QCheckBox(self.tab)
        self.checkBox_struttura.setObjectName(_fromUtf8("checkBox_struttura"))
        self.gridLayout.addWidget(self.checkBox_struttura, 3, 0, 1, 2)
        spacerItem7 = QtGui.QSpacerItem(388, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 4, 1, 2)
        self.checkBox_reperti = QtGui.QCheckBox(self.tab)
        self.checkBox_reperti.setObjectName(_fromUtf8("checkBox_reperti"))
        self.gridLayout.addWidget(self.checkBox_reperti, 4, 0, 1, 2)
        spacerItem8 = QtGui.QSpacerItem(408, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 2, 3, 1, 3)
        spacerItem9 = QtGui.QSpacerItem(438, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 3, 2, 1, 4)
        spacerItem10 = QtGui.QSpacerItem(288, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 5, 5, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(448, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 1, 1, 1, 5)
        spacerItem12 = QtGui.QSpacerItem(288, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 7, 5, 1, 1)
        self.formLayout.setLayout(1, QtGui.QFormLayout.SpanningRole, self.gridLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.comboBox_sito = QtGui.QComboBox(self.tab)
        self.comboBox_sito.setEnabled(True)
        self.comboBox_sito.setMouseTracking(False)
        self.comboBox_sito.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_sito.setAcceptDrops(False)
        self.comboBox_sito.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.comboBox_sito.setEditable(False)
        self.comboBox_sito.setDuplicatesEnabled(False)
        self.comboBox_sito.setFrame(True)
        self.comboBox_sito.setObjectName(_fromUtf8("comboBox_sito"))
        self.comboBox_sito.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox_sito)
        self.formLayout.setLayout(0, QtGui.QFormLayout.SpanningRole, self.verticalLayout)
        self.pushButton_exp_images = QtGui.QPushButton(self.tab)
        self.pushButton_exp_images.setObjectName(_fromUtf8("pushButton_exp_images"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pushButton_exp_images)
        spacerItem13 = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtGui.QFormLayout.LabelRole, spacerItem13)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog_img_exp)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_img_exp)

    def retranslateUi(self, Dialog_img_exp):
        Dialog_img_exp.setWindowTitle(
            QtGui.QApplication.translate("Dialog_img_exp", "Sistema di esportazione delle immagini", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.checkBox_tipo_reperto.setText(
            QtGui.QApplication.translate("Dialog_img_exp", "Tipo reperto", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_fase.setText(
            QtGui.QApplication.translate("Dialog_img_exp", "Fase", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_criterio_schedatura.setText(
            QtGui.QApplication.translate("Dialog_img_exp", "Criterio schedatura", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_definizione_materiale.setText(
            QtGui.QApplication.translate("Dialog_img_exp", "Definizione materiale", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.checkBox_periodo.setText(
            QtGui.QApplication.translate("Dialog_img_exp", "Periodo", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_US.setText(QtGui.QApplication.translate("Dialog_img_exp", "Unità Stratigrafiche", None,
                                                              QtGui.QApplication.UnicodeUTF8))
        self.checkBox_struttura.setText(
            QtGui.QApplication.translate("Dialog_img_exp", "Struttura", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_reperti.setText(
            QtGui.QApplication.translate("Dialog_img_exp", "Reperti", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_img_exp", "Seleziona un sito da esportare...", None,
                                                        QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sito.setItemText(0, QtGui.QApplication.translate("Dialog_img_exp", "Seleziona un valore...", None,
                                                                       QtGui.QApplication.UnicodeUTF8))
        self.pushButton_exp_images.setText(
            QtGui.QApplication.translate("Dialog_img_exp", "Esporta le immagini", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QtGui.QApplication.translate("Dialog_img_exp", "Parametri di esportazione", None,
                                                               QtGui.QApplication.UnicodeUTF8))
