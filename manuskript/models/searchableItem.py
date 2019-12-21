#!/usr/bin/env python
# --!-- coding: utf8 --!--


from manuskript.models.searchResult import searchResult
from manuskript.functions import search

class searchableItem():
    def search_occurrences(self, search_regex, columns):
        results = []
        for column in columns:
            results += [self.wrap_search_occurrence(column, startPos, endPos) for (startPos, endPos) in search(search_regex, self.search_data(column))]
        return results

    def wrap_search_occurrence(self, column, start_pos, end_pos):
        return searchResult(self.__class__.__name__, self.ID(), column, self.searchTitle(), self.searchPath(), (start_pos, end_pos))

    def searchTitle(self):
        raise NotImplementedError

    def searchPath(self):
        return ""

    def search_data(self, column):
        raise NotImplementedError
