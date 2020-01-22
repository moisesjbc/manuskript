#!/usr/bin/env python
# --!-- coding: utf8 --!--

from PyQt5.QtWidgets import QStyledItemDelegate, QLineEdit


class plotNameDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self, parent)

    def sizeHint(self, option, index):
        s = QStyledItemDelegate.sizeHint(self, option, index)
        if s.width() < 200:
            s.setWidth(200)
        return s

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setFrame(False)
        editor.setObjectName("plotNameEditor")
        return editor
