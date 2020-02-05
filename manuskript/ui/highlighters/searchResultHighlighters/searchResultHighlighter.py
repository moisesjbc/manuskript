#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.ui.highlighters.searchResultHighlighters.baseSearchResultHighlighter import baseSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.characterSearchResultHighlighter import characterSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.flatDataSearchResultHighlighter import flatDataSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.outlineSearchResultHighlighter import outlineSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.worldSearchResultHighlighter import worldSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.plotSearchResultHighlighter import plotSearchResultHighlighter
from manuskript.ui.highlighters.searchResultHighlighters.plotStepSearchResultHighlighter import plotStepSearchResultHighlighter
from manuskript.enums import SearchModel


class searchResultHighlighter(baseSearchResultHighlighter):
    """
    Highlighter for search results
    """
    def __init__(self):
        super().__init__()

    def highlightSearchResult(self, searchResult):
        """
        Highlights the given search result

        Internally holds a map associated every searchable model to its proper highlighter. This is used for delegating
        the processing to the right highlighter.
        """
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
