#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.models import references as Ref
from manuskript.enums import World
from manuskript.ui.highlighters.searchResultHighlighters.tabsSearchResultHighlighter import tabsSearchResultHighlighter
from manuskript.functions import mainWindow
from PyQt5.QtWidgets import QTextEdit, QLineEdit


class worldSearchResultHighlighter(tabsSearchResultHighlighter):
    def __init__(self):
        super().__init__(mainWindow().tabWorld)

    def openView(self, searchResult):
        r = Ref.worldReference(searchResult.id())
        Ref.open(r)

    def widgetsMap(self):
        return {
            World.name: (0, "txtWorldName", QLineEdit),
            World.description: (0, "txtWorldDescription", QTextEdit),
            World.passion: (1, "txtWorldPassion", QTextEdit),
            World.conflict: (1, "txtWorldConflict", QTextEdit)
        }
