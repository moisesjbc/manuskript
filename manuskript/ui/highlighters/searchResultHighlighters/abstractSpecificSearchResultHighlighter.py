#!/usr/bin/env python
# --!-- coding: utf8 --!--


from manuskript.ui.highlighters.searchResultHighlighters.widgetSelectionHighlighter import widgetSelectionHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.abstractSearchResultHighlighter import abstractSearchResultHighlighter


class abstractSpecificSearchResultHighlighter(abstractSearchResultHighlighter):
    def __init__(self):
        self._widgetSelectionHighlighter = widgetSelectionHighlighter()
        pass

    def highlight_search_result(self, search_result):
        self.open_view(search_result)
        widget = self.retrieve_widget(search_result)
        self._widgetSelectionHighlighter.highlight_widget_selection(widget, search_result.pos()[0], search_result.pos()[1])

    def open_view(self, search_result):
        raise RuntimeError

    def retrieve_widget(self, search_result):
        raise RuntimeError

