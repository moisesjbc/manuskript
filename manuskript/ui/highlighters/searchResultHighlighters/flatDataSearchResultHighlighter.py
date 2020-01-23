#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.functions import mainWindow
from manuskript.enums import  FlatData
from PyQt5.QtWidgets import QTextEdit, QLineEdit
from manuskript.ui.highlighters.searchResultHighlighters.abstractSpecificSearchResultHighlighter import abstractSpecificSearchResultHighlighter


class flatDataSearchResultHighlighter(abstractSpecificSearchResultHighlighter):
    def __init__(self):
        super().__init__()

    def openView(self, searchResult):
        mainWindow().tabMain.setCurrentIndex(mainWindow().TabSummary)

    def retrieveWidget(self, searchResult):
        editors = {
            FlatData.summarySituation: (0, "txtSummarySituation", QLineEdit),
            FlatData.summarySentence: (0, "txtSummarySentence", QTextEdit),
            FlatData.summaryPara: (1, "txtSummaryPara", QTextEdit),
            FlatData.summaryPage: (2, "txtSummaryPage", QTextEdit),
            FlatData.summaryFull: (3, "txtSummaryFull", QTextEdit)
        }

        stackIndex, editorName, editorClass = editors[searchResult.column()]

        mainWindow().tabSummary.setCurrentIndex(stackIndex)
        return mainWindow().tabSummary.findChild(editorClass, editorName)
