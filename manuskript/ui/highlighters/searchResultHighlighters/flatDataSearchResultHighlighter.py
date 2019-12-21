#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.functions import mainWindow
from manuskript.enums import  FlatData
from PyQt5.QtWidgets import QTextEdit, QLineEdit
from manuskript.ui.highlighters.searchResultHighlighters.abstractSpecificSearchResultHighlighter import abstractSearchResultHighlighter


class flatDataSearchResultHighlighter(abstractSearchResultHighlighter):
    def __init__(self):
        super().__init__()

    def open_view(self, search_result):
        mainWindow().tabMain.setCurrentIndex(mainWindow().TabSummary)

    def retrieve_widget(self, search_result):
        editors = {
            FlatData.summarySituation: (0, "txtSummarySituation", QLineEdit),
            FlatData.summarySentence: (0, "txtSummarySentence", QTextEdit),
            FlatData.summaryPara: (1, "txtSummaryPara", QTextEdit),
            FlatData.summaryPage: (2, "txtSummaryPage", QTextEdit),
            FlatData.summaryFull: (3, "txtSummaryFull", QTextEdit)
        }

        stack_index, editor_name, editor_class = editors[search_result.column()]

        mainWindow().tabSummary.setCurrentIndex(stack_index)
        return mainWindow().tabSummary.findChild(editor_class, editor_name)
