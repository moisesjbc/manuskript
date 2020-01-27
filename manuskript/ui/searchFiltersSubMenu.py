#!/usr/bin/env python
# --!-- coding: utf8 --!--
from PyQt5.QtWidgets import QMenu, QAction


class searchFiltersSubMenu(QMenu):
    def __init__(self, title, allSelected, items, parent=None):
        QMenu.__init__(self, parent)

        self._addAllOption(title, allSelected)
        self.addSeparator()
        self._addOptions(items, allSelected)

    def _addAllOption(self, title, selected):
        action = QAction(title, self)

        action.setText(title)
        action.setCheckable(True)
        action.setChecked(selected)
        action.triggered.connect(self._onAllTriggered)

        self.addAction(action)

    def allAction(self):
        return self.actions()[0]

    def filterActions(self):
        return self.actions()[2:]

    def _addOptions(self, items, allSelected):
        for (title, columns) in items:
            if not isinstance(columns, list):
                columns = [columns]
            action = QAction(title, self)

            action.setCheckable(True)
            action.setChecked(allSelected)
            action.setData(columns)
            action.triggered.connect(self._onFilterTriggered)

            self.addAction(action)

    def _onFilterTriggered(self):
        for action in self.filterActions():
            if not action.isChecked():
                self.allAction().setChecked(False)
                return

        self.allAction().setChecked(True)
        return

    def _onAllTriggered(self):
        for action in self.filterActions():
            action.setChecked(self.allAction().isChecked())

    def columns(self):
        columns = []
        for action in self.actions()[2:]:
            if action.isChecked():
                columns += action.data()
        return columns
