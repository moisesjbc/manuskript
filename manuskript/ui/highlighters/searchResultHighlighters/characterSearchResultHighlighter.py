#!/usr/bin/env python
# --!-- coding: utf8 --!--


from manuskript.models import references as Ref
from manuskript.functions import mainWindow
from manuskript.enums import Character
from PyQt5.QtWidgets import QTextEdit, QTableView, QLineEdit
from manuskript.ui.highlighters.searchResultHighlighters.tabsSearchResultHighlighter import tabsSearchResultHighlighter


class characterSearchResultHighlighter(tabsSearchResultHighlighter):
    def __init__(self):
        super().__init__(mainWindow().tabPersos)

    def openView(self, searchResult):
        r = Ref.characterReference(searchResult.id())
        Ref.open(r)
        mainWindow().tabPersos.setEnabled(True)

    def widgetsMap(self):
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
