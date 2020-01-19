#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.models import references as Ref
from manuskript.enums import Plot
from manuskript.ui.highlighters.searchResultHighlighters.tabsSearchResultHighlighter import tabsSearchResultHighlighter
from manuskript.functions import mainWindow
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QListView


class plotSearchResultHighlighter(tabsSearchResultHighlighter):
    def __init__(self):
        super().__init__(mainWindow().tabPlot)

    def open_view(self, search_result):
        r = Ref.plotReference(search_result.id())
        Ref.open(r)

    def widgetsMap(self):
        return {
            Plot.name: (0, "txtPlotName", QLineEdit),
            Plot.characters: (0, "lstPlotPerso", QListView),
            Plot.description: (0, "txtPlotDescription", QTextEdit),
            Plot.result: (0, "txtPlotResult", QTextEdit)
        }
