#!/usr/bin/env python
# --!-- coding: utf8 --!--


from manuskript.ui.highlighters.searchResultHighlighters.widgetSelectionHighlighter import widgetSelectionHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.baseSearchResultHighlighter import baseSearchResultHighlighter


class modelSearchResultHighlighter(baseSearchResultHighlighter):
    """
    Base class for all classes highlighting search results on model views.
    """
    def __init__(self):
        self._widgetSelectionHighlighter = widgetSelectionHighlighter()
        pass

    def highlightSearchResult(self, searchResult):
        """
        Highlight the given search result on the model view.
        """
        # Open model view
        self.openView(searchResult)

        # Retrieve the widget containing the search result
        widget = self.retrieveWidget(searchResult)

        # Highlight the search result on the retrieved widget
        self._widgetSelectionHighlighter.highlightWidgetSelection(widget, searchResult.pos()[0], searchResult.pos()[1])

    def openView(self, searchResult):
        raise RuntimeError

    def retrieveWidget(self, searchResult):
        raise RuntimeError

