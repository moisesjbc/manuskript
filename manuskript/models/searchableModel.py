#!/usr/bin/env python
# --!-- coding: utf8 --!--


class searchableModel():

    def search_occurrences(self, search_regex, columns):
        results = []
        for item in self.searchable_items():
            results += item.search_occurrences(search_regex, columns)
        return results

    def searchable_items(self):
        raise NotImplementedError
