#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.ui.highlighters.searchResultHighlighters.abstractSearchResultHighlighter import abstractSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.characterSearchResultHighlighter import characterSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.flatDataSearchResultHighlighter import flatDataSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.outlineSearchResultHighlighter import outlineSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.worldSearchResultHighlighter import worldSearchResultHighlighter

class searchResultHighlighter(abstractSearchResultHighlighter):
    def __init__(self):
        super().__init__()

    def highlight_search_result(self, search_result):
        if search_result.type() == "Character":
            highlighter = characterSearchResultHighlighter()
        elif search_result.type() == "FlatData":
            highlighter = flatDataSearchResultHighlighter()
        elif search_result.type() == "outlineItem":
            highlighter = outlineSearchResultHighlighter()
        elif search_result.type() == "World":
            highlighter = worldSearchResultHighlighter()
        else:
            raise NotImplementedError

        highlighter.highlight_search_result(search_result)
