#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.models import references as Ref
from manuskript.enums import World
from manuskript.ui.highlighters.searchResultHighlighters.tabsSearchResultHighlighter import tabsSearchResultHighlighter
from manuskript.functions import mainWindow
from PyQt5.QtWidgets import QTextEdit, QLineEdit


class worldSearchResultHighlighter(tabsSearchResultHighlighter):
    """
    Highlighter for search results on World items
    """
    def __init__(self):
        super().__init__(mainWindow().tabWorld)

    def openView(self, searchResult):
        """
        Open the world item view containing the given search result
        """
        r = Ref.worldReference(searchResult.id())
        Ref.open(r)

    def widgetsMap(self):
        """
        Returns a map associating every World searchable column to the widget containing that column.

        Result is a tuple (tabIndex, widgetName, widgetType) where:

            - tabIndex:                     index of the World item's tab containing the searched column.
            - widgetName and widgetType:    name and type of the widget containing the searched column.
        """
        return {
            World.name: (0, "txtWorldName", QLineEdit),
            World.description: (0, "txtWorldDescription", QTextEdit),
            World.passion: (1, "txtWorldPassion", QTextEdit),
            World.conflict: (1, "txtWorldConflict", QTextEdit)
        }
