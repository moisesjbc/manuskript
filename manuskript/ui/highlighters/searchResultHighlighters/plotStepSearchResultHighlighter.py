#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.models import references as Ref
from manuskript.enums import PlotStep
from manuskript.ui.highlighters.searchResultHighlighters.abstractSpecificSearchResultHighlighter import abstractSpecificSearchResultHighlighter
from manuskript.functions import mainWindow
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QTableView


class plotStepSearchResultHighlighter(abstractSpecificSearchResultHighlighter):
    def __init__(self):
        super().__init__()

    def openView(self, searchResult):
        r = Ref.plotReference(searchResult.id()[0])
        Ref.open(r)

    def retrieveWidget(self, searchResult):
        mainWindow().tabPlot.setCurrentIndex(1)
        lstSubPlots = mainWindow().tabPlot.findChild(QTableView, "lstSubPlots")

        lstSubPlots.setCurrentIndex(lstSubPlots.model().index(searchResult.id()[1], PlotStep.ID, lstSubPlots.rootIndex()))

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