#!/usr/bin/env python
# --!-- coding: utf8 --!--


from manuskript.models.searchResult import searchResult
from manuskript.functions import search


class searchableItem():
    def __init__(self, searchModel):
        self._searchModel = searchModel

    def searchOccurrences(self, searchRegex, columns):
        results = []
        for column in columns:
            results += [self.wrapSearchOccurrence(column, startPos, endPos) for (startPos, endPos) in search(searchRegex, self.searchData(column))]
        return results

    def wrapSearchOccurrence(self, column, startPos, endPos):
        return searchResult(self._searchModel, self.ID(), column, self.searchTitle(), self.searchPath(), (startPos, endPos))

    def searchTitle(self):
        raise NotImplementedError

    def searchPath(self):
        return ""

    def searchData(self, column):
        raise NotImplementedError
