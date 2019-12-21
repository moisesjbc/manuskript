#!/usr/bin/env python
# --!-- coding: utf8 --!--


from manuskript.models import references as Ref
from manuskript.functions import mainWindow
from manuskript.enums import Character
from PyQt5.QtWidgets import QTextEdit, QTableView
from manuskript.ui.highlighters.searchResultHighlighters.abstractSpecificSearchResultHighlighter import abstractSearchResultHighlighter


class characterSearchResultHighlighter(abstractSearchResultHighlighter):
    def __init__(self):
        super().__init__()

    def open_view(self, search_result):
        r = Ref.characterReference(search_result.id())
        Ref.open(r)
        mainWindow().tabPersos.setEnabled(True)

    def retrieve_widget(self, search_result):
        textEditMap = {
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

        character_tab_index, character_widget_name, character_widget_class = textEditMap[search_result.column()]

        mainWindow().tabPersos.setCurrentIndex(character_tab_index)
        return mainWindow().tabPersos.findChild(character_widget_class, character_widget_name)
