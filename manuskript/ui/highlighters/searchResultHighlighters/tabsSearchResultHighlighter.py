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

    def retrieve_widget(self, search_result):
        tab_index, widget_name, widget_class = self.widgetsMap()[search_result.column()]

        self._tabWidget.setCurrentIndex(tab_index)
        return self._tabWidget.findChild(widget_class, widget_name)
