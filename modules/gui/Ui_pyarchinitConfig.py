# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_pyarchinitConfig.ui'
#
# Created: Thu Sep 01 18:09:47 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog_Config(object):
    def setupUi(self, Dialog_Config):
        Dialog_Config.setObjectName(_fromUtf8("Dialog_Config"))
        Dialog_Config.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_Config.setEnabled(True)
        Dialog_Config.resize(636, 616)
        Dialog_Config.setMinimumSize(QtCore.QSize(450, 279))
        Dialog_Config.setMaximumSize(QtCore.QSize(1000, 1000))
        Dialog_Config.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Dialog_Config.setMouseTracking(False)
        Dialog_Config.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/iconConn.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_Config.setWindowIcon(icon)
        Dialog_Config.setAutoFillBackground(True)
        Dialog_Config.setSizeGripEnabled(False)
        Dialog_Config.setModal(True)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog_Config)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(Dialog_Config)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setProperty("resize", _fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.comboBox_Database = QtGui.QComboBox(self.tab)
        self.comboBox_Database.setEnabled(True)
        self.comboBox_Database.setMouseTracking(False)
        self.comboBox_Database.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_Database.setAcceptDrops(False)
        self.comboBox_Database.setEditable(True)
        self.comboBox_Database.setDuplicatesEnabled(False)
        self.comboBox_Database.setFrame(True)
        self.comboBox_Database.setObjectName(_fromUtf8("comboBox_Database"))
        self.comboBox_Database.addItem(_fromUtf8(""))
        self.comboBox_Database.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_Database, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_Host = QtGui.QLineEdit(self.tab)
        self.lineEdit_Host.setObjectName(_fromUtf8("lineEdit_Host"))
        self.gridLayout.addWidget(self.lineEdit_Host, 2, 1, 1, 2)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEdit_Port = QtGui.QLineEdit(self.tab)
        self.lineEdit_Port.setObjectName(_fromUtf8("lineEdit_Port"))
        self.gridLayout.addWidget(self.lineEdit_Port, 3, 1, 1, 2)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.lineEdit_DBname = QtGui.QLineEdit(self.tab)
        self.lineEdit_DBname.setObjectName(_fromUtf8("lineEdit_DBname"))
        self.gridLayout.addWidget(self.lineEdit_DBname, 4, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.lineEdit_User = QtGui.QLineEdit(self.tab)
        self.lineEdit_User.setObjectName(_fromUtf8("lineEdit_User"))
        self.gridLayout.addWidget(self.lineEdit_User, 5, 1, 1, 2)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.lineEdit_Password = QtGui.QLineEdit(self.tab)
        self.lineEdit_Password.setInputMask(_fromUtf8(""))
        self.lineEdit_Password.setText(_fromUtf8("\'\'"))
        self.lineEdit_Password.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_Password.setObjectName(_fromUtf8("lineEdit_Password"))
        self.gridLayout.addWidget(self.lineEdit_Password, 6, 1, 1, 2)
        self.pushButton_save = QtGui.QPushButton(self.tab)
        self.pushButton_save.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_save.setCheckable(False)
        self.pushButton_save.setAutoDefault(True)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.gridLayout.addWidget(self.pushButton_save, 11, 1, 1, 2)
        self.lineEdit_Logo_path = QtGui.QLineEdit(self.tab)
        self.lineEdit_Logo_path.setObjectName(_fromUtf8("lineEdit_Logo_path"))
        self.gridLayout.addWidget(self.lineEdit_Logo_path, 9, 1, 1, 2)
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 9, 0, 1, 1)
        self.lineEdit_Thumb_path = QtGui.QLineEdit(self.tab)
        self.lineEdit_Thumb_path.setObjectName(_fromUtf8("lineEdit_Thumb_path"))
        self.gridLayout.addWidget(self.lineEdit_Thumb_path, 7, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.comboBox_experimental = QtGui.QComboBox(self.tab)
        self.comboBox_experimental.setEnabled(True)
        self.comboBox_experimental.setMaximumSize(QtCore.QSize(60, 16777215))
        self.comboBox_experimental.setMouseTracking(False)
        self.comboBox_experimental.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_experimental.setAcceptDrops(False)
        self.comboBox_experimental.setEditable(True)
        self.comboBox_experimental.setDuplicatesEnabled(False)
        self.comboBox_experimental.setFrame(True)
        self.comboBox_experimental.setObjectName(_fromUtf8("comboBox_experimental"))
        self.comboBox_experimental.addItem(_fromUtf8(""))
        self.comboBox_experimental.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_experimental, 0, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.tab)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout.addWidget(self.label_26, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit_dbname = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_dbname.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_dbname.setDragEnabled(False)
        self.lineEdit_dbname.setReadOnly(False)
        self.lineEdit_dbname.setObjectName(_fromUtf8("lineEdit_dbname"))
        self.gridLayout_3.addWidget(self.lineEdit_dbname, 1, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 1, 1, 1, 1)
        self.pushButton_crea_database = QtGui.QPushButton(self.tab_2)
        self.pushButton_crea_database.setEnabled(True)
        self.pushButton_crea_database.setObjectName(_fromUtf8("pushButton_crea_database"))
        self.gridLayout_3.addWidget(self.pushButton_crea_database, 1, 2, 2, 1)
        self.lineEdit_template_postgis = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_template_postgis.setObjectName(_fromUtf8("lineEdit_template_postgis"))
        self.gridLayout_3.addWidget(self.lineEdit_template_postgis, 2, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 2, 1, 1, 1)
        self.lineEdit_port_db = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_port_db.setObjectName(_fromUtf8("lineEdit_port_db"))
        self.gridLayout_3.addWidget(self.lineEdit_port_db, 3, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.tab_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 3, 1, 1, 1)
        self.pyarchinit_progressBar_db = QtGui.QProgressBar(self.tab_2)
        self.pyarchinit_progressBar_db.setProperty("value", 1)
        self.pyarchinit_progressBar_db.setAlignment(QtCore.Qt.AlignCenter)
        self.pyarchinit_progressBar_db.setOrientation(QtCore.Qt.Horizontal)
        self.pyarchinit_progressBar_db.setInvertedAppearance(False)
        self.pyarchinit_progressBar_db.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.pyarchinit_progressBar_db.setObjectName(_fromUtf8("pyarchinit_progressBar_db"))
        self.gridLayout_3.addWidget(self.pyarchinit_progressBar_db, 4, 0, 1, 1)
        self.pushButton_crea_layer = QtGui.QPushButton(self.tab_2)
        self.pushButton_crea_layer.setEnabled(True)
        self.pushButton_crea_layer.setObjectName(_fromUtf8("pushButton_crea_layer"))
        self.gridLayout_3.addWidget(self.pushButton_crea_layer, 4, 2, 2, 1)
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 2)
        self.pyarchinit_progressBar_template = QtGui.QProgressBar(self.tab_2)
        self.pyarchinit_progressBar_template.setProperty("value", 1)
        self.pyarchinit_progressBar_template.setAlignment(QtCore.Qt.AlignCenter)
        self.pyarchinit_progressBar_template.setOrientation(QtCore.Qt.Horizontal)
        self.pyarchinit_progressBar_template.setInvertedAppearance(False)
        self.pyarchinit_progressBar_template.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.pyarchinit_progressBar_template.setObjectName(_fromUtf8("pyarchinit_progressBar_template"))
        self.gridLayout_3.addWidget(self.pyarchinit_progressBar_template, 6, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 6, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 7, 0, 1, 2)
        self.pushButton_crea_layer_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_crea_layer_2.setEnabled(True)
        self.pushButton_crea_layer_2.setObjectName(_fromUtf8("pushButton_crea_layer_2"))
        self.gridLayout_3.addWidget(self.pushButton_crea_layer_2, 7, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 259, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 8, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.comboBox_mapper_read = QtGui.QComboBox(self.tab_3)
        self.comboBox_mapper_read.setObjectName(_fromUtf8("comboBox_mapper_read"))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.comboBox_mapper_read, 5, 3, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_6.addWidget(self.label_11, 0, 1, 1, 1)
        self.lineEdit_pass_rd = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_pass_rd.setObjectName(_fromUtf8("lineEdit_pass_rd"))
        self.gridLayout_6.addWidget(self.lineEdit_pass_rd, 8, 5, 1, 1)
        self.pushButton_exp_directories = QtGui.QPushButton(self.tab_3)
        self.pushButton_exp_directories.setObjectName(_fromUtf8("pushButton_exp_directories"))
        self.gridLayout_6.addWidget(self.pushButton_exp_directories, 2, 1, 1, 1)
        self.comboBox_server_rd = QtGui.QComboBox(self.tab_3)
        self.comboBox_server_rd.setObjectName(_fromUtf8("comboBox_server_rd"))
        self.comboBox_server_rd.addItem(_fromUtf8(""))
        self.comboBox_server_rd.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.comboBox_server_rd, 7, 1, 1, 1)
        self.line = QtGui.QFrame(self.tab_3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_6.addWidget(self.line, 3, 1, 1, 5)
        self.lineEdit_username_rd = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_username_rd.setObjectName(_fromUtf8("lineEdit_username_rd"))
        self.gridLayout_6.addWidget(self.lineEdit_username_rd, 8, 3, 1, 2)
        self.label_18 = QtGui.QLabel(self.tab_3)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_6.addWidget(self.label_18, 10, 3, 1, 1)
        self.label_22 = QtGui.QLabel(self.tab_3)
        self.label_22.setText(_fromUtf8(""))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_6.addWidget(self.label_22, 22, 5, 1, 1)
        self.label_17 = QtGui.QLabel(self.tab_3)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_6.addWidget(self.label_17, 10, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.tab_3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_6.addWidget(self.label_19, 10, 5, 1, 1)
        self.label_27 = QtGui.QLabel(self.tab_3)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_6.addWidget(self.label_27, 32, 1, 1, 1)
        self.lineEdit_host_wt = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_host_wt.setObjectName(_fromUtf8("lineEdit_host_wt"))
        self.gridLayout_6.addWidget(self.lineEdit_host_wt, 31, 1, 1, 1)
        self.lineEdit_username_wt = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_username_wt.setObjectName(_fromUtf8("lineEdit_username_wt"))
        self.gridLayout_6.addWidget(self.lineEdit_username_wt, 31, 3, 1, 2)
        self.lineEdit_pass_wt = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_pass_wt.setObjectName(_fromUtf8("lineEdit_pass_wt"))
        self.gridLayout_6.addWidget(self.lineEdit_pass_wt, 31, 5, 1, 1)
        self.lineEdit_database_wt = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_database_wt.setObjectName(_fromUtf8("lineEdit_database_wt"))
        self.gridLayout_6.addWidget(self.lineEdit_database_wt, 33, 1, 1, 1)
        self.label_29 = QtGui.QLabel(self.tab_3)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_6.addWidget(self.label_29, 32, 5, 1, 1)
        self.label_28 = QtGui.QLabel(self.tab_3)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_6.addWidget(self.label_28, 32, 3, 1, 1)
        self.label_24 = QtGui.QLabel(self.tab_3)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_6.addWidget(self.label_24, 34, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 68, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 36, 1, 1, 1)
        self.label_60 = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.gridLayout_6.addWidget(self.label_60, 6, 1, 1, 1)
        self.label_61 = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.gridLayout_6.addWidget(self.label_61, 28, 1, 1, 1)
        self.lineEdit_host_rd = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_host_rd.setObjectName(_fromUtf8("lineEdit_host_rd"))
        self.gridLayout_6.addWidget(self.lineEdit_host_rd, 8, 1, 1, 1)
        self.lineEdit_database_rd = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_database_rd.setObjectName(_fromUtf8("lineEdit_database_rd"))
        self.gridLayout_6.addWidget(self.lineEdit_database_rd, 12, 1, 1, 1)
        self.label_59 = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.gridLayout_6.addWidget(self.label_59, 5, 1, 1, 1)
        self.label_62 = QtGui.QLabel(self.tab_3)
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.gridLayout_6.addWidget(self.label_62, 18, 1, 1, 1)
        self.lineEdit_port_rd = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_port_rd.setObjectName(_fromUtf8("lineEdit_port_rd"))
        self.gridLayout_6.addWidget(self.lineEdit_port_rd, 12, 2, 1, 1)
        self.label_20 = QtGui.QLabel(self.tab_3)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_6.addWidget(self.label_20, 13, 1, 1, 1)
        self.pushButton_import = QtGui.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_import.setFont(font)
        self.pushButton_import.setObjectName(_fromUtf8("pushButton_import"))
        self.gridLayout_6.addWidget(self.pushButton_import, 35, 5, 1, 1)
        self.lineEdit_value_rd = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_value_rd.setObjectName(_fromUtf8("lineEdit_value_rd"))
        self.gridLayout_6.addWidget(self.lineEdit_value_rd, 15, 2, 1, 2)
        self.label_25 = QtGui.QLabel(self.tab_3)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_6.addWidget(self.label_25, 13, 2, 1, 1)
        self.lineEdit_field_rd = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_field_rd.setObjectName(_fromUtf8("lineEdit_field_rd"))
        self.gridLayout_6.addWidget(self.lineEdit_field_rd, 15, 1, 1, 1)
        self.label_23 = QtGui.QLabel(self.tab_3)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_6.addWidget(self.label_23, 18, 2, 1, 1)
        self.lineEdit_port_wt = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_port_wt.setObjectName(_fromUtf8("lineEdit_port_wt"))
        self.gridLayout_6.addWidget(self.lineEdit_port_wt, 33, 2, 1, 1)
        self.label_21 = QtGui.QLabel(self.tab_3)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_6.addWidget(self.label_21, 6, 3, 1, 1)
        self.label_57 = QtGui.QLabel(self.tab_3)
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.gridLayout_6.addWidget(self.label_57, 34, 2, 1, 1)
        self.comboBox_server_wt = QtGui.QComboBox(self.tab_3)
        self.comboBox_server_wt.setMinimumSize(QtCore.QSize(20, 0))
        self.comboBox_server_wt.setObjectName(_fromUtf8("comboBox_server_wt"))
        self.comboBox_server_wt.addItem(_fromUtf8(""))
        self.comboBox_server_wt.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.comboBox_server_wt, 29, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog_Config)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Config)
        Dialog_Config.setTabOrder(self.comboBox_Database, self.lineEdit_Host)
        Dialog_Config.setTabOrder(self.lineEdit_Host, self.lineEdit_Port)
        Dialog_Config.setTabOrder(self.lineEdit_Port, self.lineEdit_DBname)
        Dialog_Config.setTabOrder(self.lineEdit_DBname, self.lineEdit_User)
        Dialog_Config.setTabOrder(self.lineEdit_User, self.lineEdit_Password)

    def retranslateUi(self, Dialog_Config):
        Dialog_Config.setWindowTitle(_translate("Dialog_Config", "Impostazioni del sistema", None))
        self.label.setText(_translate("Dialog_Config", "Database", None))
        self.comboBox_Database.setItemText(0, _translate("Dialog_Config", "postgres", None))
        self.comboBox_Database.setItemText(1, _translate("Dialog_Config", "sqlite", None))
        self.label_2.setText(_translate("Dialog_Config", "Host", None))
        self.lineEdit_Host.setText(_translate("Dialog_Config", "\'\'", None))
        self.label_7.setText(_translate("Dialog_Config", "Port", None))
        self.lineEdit_Port.setText(_translate("Dialog_Config", "\'\'", None))
        self.label_3.setText(_translate("Dialog_Config", "DBname", None))
        self.lineEdit_DBname.setText(_translate("Dialog_Config", "\'\'", None))
        self.label_4.setText(_translate("Dialog_Config", "User", None))
        self.lineEdit_User.setText(_translate("Dialog_Config", "\'\'", None))
        self.label_5.setText(_translate("Dialog_Config", "Password", None))
        self.pushButton_save.setText(_translate("Dialog_Config", "Salva i parametri", None))
        self.lineEdit_Logo_path.setText(_translate("Dialog_Config", "\'\'", None))
        self.label_16.setText(_translate("Dialog_Config", "Logo path", None))
        self.lineEdit_Thumb_path.setText(_translate("Dialog_Config", "\'\'", None))
        self.label_10.setText(_translate("Dialog_Config", "Thumbnail path", None))
        self.comboBox_experimental.setItemText(0, _translate("Dialog_Config", "Si", None))
        self.comboBox_experimental.setItemText(1, _translate("Dialog_Config", "No", None))
        self.label_26.setText(_translate("Dialog_Config", "Experimental", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  _translate("Dialog_Config", "Parametri di connessione", None))
        self.label_6.setText(_translate("Dialog_Config", "Installa il database", None))
        self.lineEdit_dbname.setText(_translate("Dialog_Config", "pyarchinit", None))
        self.label_12.setToolTip(_translate("Dialog_Config",
                                            "<html><head/><body><p><span style=\" font-size:10pt;\">Puoi inserire un nome differente da quello presente</span></p></body></html>",
                                            None))
        self.label_12.setText(_translate("Dialog_Config", "inserisci nome db", None))
        self.pushButton_crea_database.setText(_translate("Dialog_Config", "Installa", None))
        self.lineEdit_template_postgis.setText(_translate("Dialog_Config", "template_postgis_20", None))
        self.label_13.setToolTip(_translate("Dialog_Config",
                                            "<html><head/><body><p>qui devi inserire il nome del template che vuoi usare. Ricorda di usare il template specifico a seconda di quale postgis usi</p></body></html>",
                                            None))
        self.label_13.setText(_translate("Dialog_Config", "inserisci nome template", None))
        self.lineEdit_port_db.setText(_translate("Dialog_Config", "5432", None))
        self.label_15.setToolTip(_translate("Dialog_Config",
                                            "<html><head/><body><p><span style=\" font-size:10pt;\">puoi inserire il numero di porta differente</span></p></body></html>",
                                            None))
        self.label_15.setText(_translate("Dialog_Config", "inserisci numero porta", None))
        self.pushButton_crea_layer.setText(_translate("Dialog_Config", "Installa", None))
        self.label_8.setText(_translate("Dialog_Config", "Installa il db geografico su Postgres per postgis 1.5", None))
        self.label_14.setText(_translate("Dialog_Config",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">OPPURE</span></p></body></html>",
                                         None))
        self.label_9.setText(_translate("Dialog_Config", "Installa il db geografico su Postgres per postgis 2.x", None))
        self.pushButton_crea_layer_2.setText(_translate("Dialog_Config", "Installa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("Dialog_Config", "Installazione layers", None))
        self.comboBox_mapper_read.setItemText(0, _translate("Dialog_Config", "US", None))
        self.comboBox_mapper_read.setItemText(1, _translate("Dialog_Config", "UT", None))
        self.comboBox_mapper_read.setItemText(2, _translate("Dialog_Config", "SITE", None))
        self.comboBox_mapper_read.setItemText(3, _translate("Dialog_Config", "PERIODIZZAZIONE", None))
        self.comboBox_mapper_read.setItemText(4, _translate("Dialog_Config", "INVENTARIO_MATERIALI", None))
        self.comboBox_mapper_read.setItemText(5, _translate("Dialog_Config", "STRUTTURA", None))
        self.comboBox_mapper_read.setItemText(6, _translate("Dialog_Config", "TAFONOMIA", None))
        self.comboBox_mapper_read.setItemText(7, _translate("Dialog_Config", "PYARCHINIT_THESAURUS", None))
        self.comboBox_mapper_read.setItemText(8, _translate("Dialog_Config", "SCHEDAIND", None))
        self.comboBox_mapper_read.setItemText(9, _translate("Dialog_Config", "DETSESSO", None))
        self.comboBox_mapper_read.setItemText(10, _translate("Dialog_Config", "DETETA", None))
        self.comboBox_mapper_read.setItemText(11, _translate("Dialog_Config", "ARCHEOZOOLOGY", None))
        self.comboBox_mapper_read.setItemText(12, _translate("Dialog_Config", "CAMPIONI", None))
        self.comboBox_mapper_read.setItemText(13, _translate("Dialog_Config", "DOCUMENTAZIONE", None))
        self.label_11.setText(_translate("Dialog_Config", "Esportazione directories", None))
        self.pushButton_exp_directories.setText(_translate("Dialog_Config", "Esportazione experimental", None))
        self.comboBox_server_rd.setItemText(0, _translate("Dialog_Config", "sqlite", None))
        self.comboBox_server_rd.setItemText(1, _translate("Dialog_Config", "postgres", None))
        self.label_18.setText(_translate("Dialog_Config", "Username", None))
        self.label_17.setText(_translate("Dialog_Config", "Host", None))
        self.label_19.setText(_translate("Dialog_Config", "Password", None))
        self.label_27.setText(_translate("Dialog_Config", "Host", None))
        self.label_29.setText(_translate("Dialog_Config", "Password", None))
        self.label_28.setText(_translate("Dialog_Config", "Username", None))
        self.label_24.setText(_translate("Dialog_Config", "Database", None))
        self.label_60.setText(_translate("Dialog_Config", "FROM", None))
        self.label_61.setText(_translate("Dialog_Config", "TO", None))
        self.label_59.setText(_translate("Dialog_Config", "Importazione dati", None))
        self.label_62.setText(_translate("Dialog_Config", "Nome campo", None))
        self.label_20.setText(_translate("Dialog_Config", "Database", None))
        self.pushButton_import.setText(_translate("Dialog_Config", "Import", None))
        self.label_25.setText(_translate("Dialog_Config", "Port", None))
        self.label_23.setText(_translate("Dialog_Config", "Valore", None))
        self.label_21.setText(_translate("Dialog_Config", "Mappatura pyArchInit", None))
        self.label_57.setText(_translate("Dialog_Config", "Port", None))
        self.comboBox_server_wt.setItemText(0, _translate("Dialog_Config", "postgres", None))
        self.comboBox_server_wt.setItemText(1, _translate("Dialog_Config", "sqlite", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  _translate("Dialog_Config", "Tool di importazione", None))
