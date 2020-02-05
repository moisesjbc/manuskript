#!/usr/bin/env python
# --!-- coding: utf8 --!--


from manuskript.models import references as Ref
from manuskript.functions import mainWindow
from manuskript.enums import Character
from PyQt5.QtWidgets import QTextEdit, QTableView, QLineEdit
from manuskript.ui.highlighters.searchResultHighlighters.tabsSearchResultHighlighter import tabsSearchResultHighlighter


class characterSearchResultHighlighter(tabsSearchResultHighlighter):
    """
    Highlighter for search results on characters
    """
    def __init__(self):
        super().__init__(mainWindow().tabPersos)

    def openView(self, searchResult):
        """
        Open the character view containing the given search result
        """
        r = Ref.characterReference(searchResult.id())
        Ref.open(r)
        mainWindow().tabPersos.setEnabled(True)

    def widgetsMap(self):
        """
        Returns a map associating every character searchable column to the widget containing that column.

        Result is a tuple (tabIndex, widgetName, widgetType) where:

            - tabIndex:                     index of the Character's tab containing the searched column.
            - widgetName and widgetType:    name and type of the widget containing the searched column.
        """
        return {
            Character.name: (0, "txtPersoName", QLineEdit),
            Character.goal: (0, "txtPersoGoal", QTextEdit),
            Character.motivation: (0, "txtPersoMotivation", QTextEdit),
            Character.conflict: (0, "txtPersoConflict", QTextEdit),
            Character.epiphany: (0, "txtPersoEpiphany", QTextEdit),
            Character.summarySentence: (0, "txtPersoSummarySentence", QTextEdit),
            Character.summaryPara: (0, "txtPersoSummaryPara", QTextEdit),
            Character.summaryFull: (1, "txtPersoSummaryFull", QTextEdit),
            Character.notes: (2, "txtPersoNotes", QTextEdit),
            Character.infos: (3, "tblPersoInfos", QTableView)
        }
