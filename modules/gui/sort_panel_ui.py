# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/pyarchinit/.qgis/python/plugins/pyarchinit/modules/gui/sort_panel_ui.ui'
#
# Created: Thu Jan 28 21:25:39 2010
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_sortPanel(object):
    def setupUi(self, sortPanel):
        sortPanel.setObjectName("sortPanel")
        sortPanel.setWindowModality(QtCore.Qt.NonModal)
        sortPanel.resize(635, 340)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sortPanel.setWindowIcon(icon)
        self.gridlayout = QtGui.QGridLayout(sortPanel)
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtGui.QLabel(sortPanel)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(387, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 0, 1, 1, 4)
        self.FieldsList = QtGui.QListWidget(sortPanel)
        self.FieldsList.setAcceptDrops(True)
        self.FieldsList.setEditTriggers(
            QtGui.QAbstractItemView.DoubleClicked | QtGui.QAbstractItemView.EditKeyPressed | QtGui.QAbstractItemView.SelectedClicked)
        self.FieldsList.setDragEnabled(True)
        self.FieldsList.setDragDropOverwriteMode(True)
        self.FieldsList.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.FieldsList.setAlternatingRowColors(True)
        self.FieldsList.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.FieldsList.setViewMode(QtGui.QListView.ListMode)
        self.FieldsList.setObjectName("FieldsList")
        self.gridlayout.addWidget(self.FieldsList, 1, 0, 7, 2)
        spacerItem1 = QtGui.QSpacerItem(41, 81, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem1, 1, 2, 3, 1)
        self.FieldListsort = QtGui.QListWidget(sortPanel)
        self.FieldListsort.setAcceptDrops(True)
        self.FieldListsort.setAutoScroll(False)
        self.FieldListsort.setEditTriggers(
            QtGui.QAbstractItemView.DoubleClicked | QtGui.QAbstractItemView.EditKeyPressed)
        self.FieldListsort.setProperty("showDropIndicator", False)
        self.FieldListsort.setDragEnabled(False)
        self.FieldListsort.setDragDropOverwriteMode(False)
        self.FieldListsort.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.FieldListsort.setAlternatingRowColors(True)
        self.FieldListsort.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.FieldListsort.setMovement(QtGui.QListView.Free)
        self.FieldListsort.setViewMode(QtGui.QListView.ListMode)
        self.FieldListsort.setObjectName("FieldListsort")
        self.gridlayout.addWidget(self.FieldListsort, 1, 3, 7, 1)
        self.radioButtonAsc = QtGui.QRadioButton(sortPanel)
        self.radioButtonAsc.setChecked(True)
        self.radioButtonAsc.setObjectName("radioButtonAsc")
        self.gridlayout.addWidget(self.radioButtonAsc, 1, 4, 1, 1)
        self.radioButtonDisc = QtGui.QRadioButton(sortPanel)
        self.radioButtonDisc.setObjectName("radioButtonDisc")
        self.gridlayout.addWidget(self.radioButtonDisc, 2, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(91, 171, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem2, 3, 4, 4, 1)
        self.pushButtonRight = QtGui.QPushButton(sortPanel)
        self.pushButtonRight.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/6_rightArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRight.setIcon(icon1)
        self.pushButtonRight.setCheckable(False)
        self.pushButtonRight.setAutoDefault(True)
        self.pushButtonRight.setObjectName("pushButtonRight")
        self.gridlayout.addWidget(self.pushButtonRight, 4, 2, 1, 1)
        self.pushButtonLeft = QtGui.QPushButton(sortPanel)
        self.pushButtonLeft.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/4_leftArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLeft.setIcon(icon2)
        self.pushButtonLeft.setCheckable(False)
        self.pushButtonLeft.setAutoDefault(True)
        self.pushButtonLeft.setObjectName("pushButtonLeft")
        self.gridlayout.addWidget(self.pushButtonLeft, 5, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(41, 121, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem3, 6, 2, 2, 1)
        self.pushButtonSort = QtGui.QPushButton(sortPanel)
        self.pushButtonSort.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonSort.setCheckable(False)
        self.pushButtonSort.setAutoDefault(True)
        self.pushButtonSort.setObjectName("pushButtonSort")
        self.gridlayout.addWidget(self.pushButtonSort, 7, 4, 1, 1)

        self.retranslateUi(sortPanel)
        QtCore.QMetaObject.connectSlotsByName(sortPanel)

    def retranslateUi(self, sortPanel):
        sortPanel.setWindowTitle(
            QtGui.QApplication.translate("sortPanel", "Ordina", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("sortPanel", "Criteri di ordinamento", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonAsc.setText(
            QtGui.QApplication.translate("sortPanel", "Ascendente", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonDisc.setText(
            QtGui.QApplication.translate("sortPanel", "Discendente", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSort.setText(
            QtGui.QApplication.translate("sortPanel", "Ordina", None, QtGui.QApplication.UnicodeUTF8))
