#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.models import references as Ref
from manuskript.enums import Plot
from manuskript.ui.highlighters.searchResultHighlighters.tabsSearchResultHighlighter import tabsSearchResultHighlighter
from manuskript.functions import mainWindow
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QListView


class plotSearchResultHighlighter(tabsSearchResultHighlighter):
    """
    Highlighter for search results on plot items
    """
    def __init__(self):
        super().__init__(mainWindow().tabPlot)

    def openView(self, searchResult):
        """
        Open the plot view containing the given search result
        """
        r = Ref.plotReference(searchResult.id())
        Ref.open(r)

    def widgetsMap(self):
        """
        Returns a map associating every plot searchable column to the widget containing that column.

        Result is a tuple (tabIndex, widgetName, widgetType) where:

            - tabIndex:                     index of the Plot's tab containing the searched column.
            - widgetName and widgetType:    name and type of the widget containing the searched column.
        """
        return {
            Plot.name: (0, "txtPlotName", QLineEdit),
            Plot.characters: (0, "lstPlotPerso", QListView),
            Plot.description: (0, "txtPlotDescription", QTextEdit),
            Plot.result: (0, "txtPlotResult", QTextEdit)
        }
