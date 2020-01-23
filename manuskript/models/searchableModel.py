#!/usr/bin/env python
# --!-- coding: utf8 --!--


class searchableModel():

    def searchOccurrences(self, searchRegex, columns):
        results = []
        for item in self.searchableItems():
            results += item.searchOccurrences(searchRegex, columns)
        return results

    def searchableItems(self):
        raise NotImplementedError
