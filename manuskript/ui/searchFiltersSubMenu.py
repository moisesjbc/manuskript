#!/usr/bin/env python
# --!-- coding: utf8 --!--
from PyQt5.QtWidgets import QMenu, QAction


class searchFiltersSubMenu(QMenu):
    def __init__(self, title, all_selected, items, parent=None):
        QMenu.__init__(self, parent)

        self._add_all_option(title, all_selected)
        self.addSeparator()
        self._add_options(items, all_selected)

    def _add_all_option(self, title, selected):
        action = QAction(self.tr(title), self)

        action.setText(title)
        action.setCheckable(True)
        action.setChecked(selected)
        action.triggered.connect(self._on_all_triggered)

        self.addAction(action)

    def allAction(self):
        return self.actions()[0]

    def filterActions(self):
        return self.actions()[2:]

    def _add_options(self, items, all_selected):
        for (title, column) in items:
            action = QAction(self.tr(title), self)

            action.setCheckable(True)
            action.setChecked(all_selected)
            action.setData(column)
            action.triggered.connect(self._on_filter_triggered)

            self.addAction(action)

    def _on_filter_triggered(self):
        for action in self.filterActions():
            if not action.isChecked():
                self.allAction().setChecked(False)
                return

        self.allAction().setChecked(True)
        return

    def _on_all_triggered(self):
        for action in self.filterActions():
            action.setChecked(self.allAction().isChecked())

    def columns(self):
        columns = []
        for action in self.actions()[2:]:
            if action.isChecked():
                columns.append(action.data())
        return columns
