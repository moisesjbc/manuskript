#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.ui.highlighters.searchResultHighlighters.widgetSelectionHighlighter import widgetSelectionHighlighter
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QTableWidget, QListWidget, QComboBox, QTableWidgetItem


def test_highlightTextEdit():
    textEdit = QTextEdit("Text to be searched: foo")
    widgetSelectionHighlighter().highlightWidgetSelection(textEdit, 5, 19)
    assert textEdit.textCursor().selectedText() == "to be searched"


def test_highlightLineEdit():
    lineEdit = QLineEdit("Text to be searched: foo")
    widgetSelectionHighlighter().highlightWidgetSelection(lineEdit, 5, 10)
    assert lineEdit.selectedText() == "to be"


def test_highligtTableView():
    tableView = QTableWidget()
    tableView.setRowCount(2)
    tableView.setColumnCount(2)
    tableView.setItem(0, 0, QTableWidgetItem("0, 0"))
    tableView.setItem(0, 1, QTableWidgetItem("0, 1"))
    tableView.setItem(1, 0, QTableWidgetItem("1, 0"))
    tableView.setItem(1, 1, QTableWidgetItem("1, 1"))

    # End pos is ignored. All row at startPos is selected.
    widgetSelectionHighlighter().highlightWidgetSelection(tableView, 1, 9999)

    selectedItems = tableView.selectedItems()
    assert len(selectedItems) == 2
    assert selectedItems[0].text() == "1, 0"
    assert selectedItems[1].text() == "1, 1"


def test_highligtListView():
    listView = QListWidget()
    listView.addItem("A")
    listView.addItem("B")
    listView.addItem("C")

    # End pos is ignored. Item at startPos is selected.
    widgetSelectionHighlighter().highlightWidgetSelection(listView, 1, 9999)

    selectedItems = listView.selectedItems()
    assert len(selectedItems) == 1
    assert selectedItems[0].text() == "B"


def test_highlightComboBox():
    comboBox = QComboBox()
    comboBox.setStyleSheet("color: red;")
    assert comboBox.styleSheet() == "color: red;"

    # startPos and endPos are ignored.
    widgetSelectionHighlighter().highlightWidgetSelection(comboBox, 9999, 9999)
    assert comboBox.styleSheet() == "color: red; background-color: steelblue;"
