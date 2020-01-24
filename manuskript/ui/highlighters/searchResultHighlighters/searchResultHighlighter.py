#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.ui.highlighters.searchResultHighlighters.abstractSearchResultHighlighter import abstractSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.characterSearchResultHighlighter import characterSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.flatDataSearchResultHighlighter import flatDataSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.outlineSearchResultHighlighter import outlineSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.worldSearchResultHighlighter import worldSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.plotSearchResultHighlighter import plotSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.plotStepSearchResultHighlighter import plotStepSearchResultHighlighter
from manuskript.enums import SearchModel


class searchResultHighlighter(abstractSearchResultHighlighter):
    def __init__(self):
        super().__init__()

    def highlightSearchResult(self, searchResult):
        highlighters = {
            SearchModel.outline: outlineSearchResultHighlighter,
            SearchModel.character: characterSearchResultHighlighter,
            SearchModel.flatData: flatDataSearchResultHighlighter,
            SearchModel.world: worldSearchResultHighlighter,
            SearchModel.plot: plotSearchResultHighlighter,
            SearchModel.plotStep: plotStepSearchResultHighlighter
        }
        highlighter = highlighters[searchResult.type()]()

        highlighter.highlightSearchResult(searchResult)
