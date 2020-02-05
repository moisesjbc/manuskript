#!/usr/bin/env python
# --!-- coding: utf8 --!--


class baseSearchResultHighlighter():
    """
    Base interface for all classes highlighting search results on model views.
    """
    def highlightSearchResult(self, searchResult):
        """
        Highlight the given searchResult instance
        """
        raise NotImplementedError
