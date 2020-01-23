#!/usr/bin/env python
# --!-- coding: utf8 --!--


from manuskript.ui.highlighters.searchResultHighlighters.abstractSpecificSearchResultHighlighter import abstractSpecificSearchResultHighlighter


class tabsSearchResultHighlighter(abstractSpecificSearchResultHighlighter):
    """
    Base class for Character and World highlighters: the ones highlighting widgets inside a QTabWidget.
    """
    def __init__(self, tabWidget):
        super().__init__()
        self._tabWidget = tabWidget

    def widgetsMap(self):
        raise RuntimeError

    def retrieveWidget(self, searchResult):
        tabIndex, widgetName, widgetClass = self.widgetsMap()[searchResult.column()]

        self._tabWidget.setEnabled(True)
        self._tabWidget.setCurrentIndex(tabIndex)
        return self._tabWidget.findChild(widgetClass, widgetName)
