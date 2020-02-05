#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.functions import mainWindow
from manuskript.enums import  FlatData
from PyQt5.QtWidgets import QTextEdit, QLineEdit
from manuskript.ui.highlighters.searchResultHighlighters.modelSearchResultHighlighter import modelSearchResultHighlighter


class flatDataSearchResultHighlighter(modelSearchResultHighlighter):
    """
    Highlighter for search results on flat data
    """
    def __init__(self):
        super().__init__()

    def openView(self, searchResult):
        """
        Open the flat data view
        """
        mainWindow().tabMain.setCurrentIndex(mainWindow().TabSummary)

    def retrieveWidget(self, searchResult):
        """
        Retrieves the widget containing the given search result.

        Internally uses a map associating every searchable column to a tuple (stackIndex, widgetName, widgetType) where:

            - stackIndex:                   index of the FlatData's tab stacked widget containing the searched column.
            - widgetName and widgetType:    name and type of the widget containing the searched column.
        """
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
