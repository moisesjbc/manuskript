#!/usr/bin/env python
# --!-- coding: utf8 --!--


from manuskript.ui.highlighters.searchResultHighlighters.widgetSelectionHighlighter import widgetSelectionHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.abstractSearchResultHighlighter import abstractSearchResultHighlighter


class abstractSpecificSearchResultHighlighter(abstractSearchResultHighlighter):
    def __init__(self):
        self._widgetSelectionHighlighter = widgetSelectionHighlighter()
        pass

    def highlightSearchResult(self, searchResult):
        self.openView(searchResult)
        widget = self.retrieveWidget(searchResult)
        self._widgetSelectionHighlighter.highlightWidgetSelection(widget, searchResult.pos()[0], searchResult.pos()[1])

    def openView(self, searchResult):
        raise RuntimeError

    def retrieveWidget(self, searchResult):
        raise RuntimeError

