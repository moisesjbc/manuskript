#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.models import references as Ref
from manuskript.enums import PlotStep
from manuskript.ui.highlighters.searchResultHighlighters.modelSearchResultHighlighter import modelSearchResultHighlighter
from manuskript.functions import mainWindow
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QTableView


class plotStepSearchResultHighlighter(modelSearchResultHighlighter):
    """
    Highlighter for search results on plot step items
    """
    def __init__(self):
        super().__init__()

    def openView(self, searchResult):
        """
        Open the plot step view containing the given search result
        """
        r = Ref.plotReference(searchResult.id()[0])
        Ref.open(r)

    def retrieveWidget(self, searchResult):
        """
        Retrieves the widget containing the given search result.

        Internally uses a map associating every searchable column to a tuple (widgetName, widgetType) where:

            - widgetName and widgetType:    name and type of the widget containing the searched column.
        """
        mainWindow().tabPlot.setCurrentIndex(1)
        lstSubPlots = mainWindow().tabPlot.findChild(QTableView, "lstSubPlots")

        lstSubPlots.setCurrentIndex(lstSubPlots.model().index(searchResult.id()[1], PlotStep.ID, lstSubPlots.rootIndex()))

        # This fixes the following bug:
        #
        # 1. Click on a search result referencing a plot step summary.
        # 2. Click on another plot
        # 3. Click again on the previous search result.
        #
        # Without emitting the clicked signal, the plot step summary edit is not activated.
        lstSubPlots.clicked.emit(lstSubPlots.currentIndex())

        if searchResult.column() == PlotStep.name:
            # For plot step names, we trigger an edition on the plot steps list. By doing this, an editor is created
            # for that plot so we can highlight it later.
            lstSubPlots.edit(lstSubPlots.model().index(searchResult.id()[1], 0, lstSubPlots.rootIndex()))

        if lstSubPlots.currentIndex().isValid():
            widgetsMap = {
                PlotStep.name: ("plotNameEditor", QLineEdit),
                PlotStep.summary: ("txtSubPlotSummary", QTextEdit)
            }

            widgetName, widgetClass = widgetsMap[searchResult.column()]
            return mainWindow().tabPlot.findChild(widgetClass, widgetName)
        else:
            return None