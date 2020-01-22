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

    def open_view(self, search_result):
        r = Ref.plotReference(search_result.id()[0])
        Ref.open(r)

    def retrieve_widget(self, search_result):
        mainWindow().tabPlot.setCurrentIndex(1)
        lstSubPlots = mainWindow().tabPlot.findChild(QTableView, "lstSubPlots")

        lstSubPlots.setCurrentIndex(lstSubPlots.model().index(search_result.id()[1], PlotStep.ID, lstSubPlots.rootIndex()))

        if search_result.column() == PlotStep.name:
            # For plot step names, we trigger an edition on the plot steps list. By doing this, an editor is created
            # for that plot so we can highlight it later.
            lstSubPlots.edit(lstSubPlots.model().index(search_result.id()[1], 0, lstSubPlots.rootIndex()))

        if lstSubPlots.currentIndex().isValid():
            widgetsMap = {
                PlotStep.name: ("plotNameEditor", QLineEdit),
                PlotStep.summary: ("txtSubPlotSummary", QTextEdit)
            }

            widgetName, widgetClass = widgetsMap[search_result.column()]
            return mainWindow().tabPlot.findChild(widgetClass, widgetName)
        else:
            return None