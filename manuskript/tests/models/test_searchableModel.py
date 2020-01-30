#!/usr/bin/env python
# --!-- coding: utf8 --!--

import re
from manuskript.models.searchableModel import searchableModel


class searchableItemMock:
    def __init__(self, dummyOccurrence):
        self.dummyOccurrence = dummyOccurrence

    def searchOccurrences(self, regex, columns):
        return ["({}, {}, {})".format(self.dummyOccurrence, regex, columns)]


def test_searchableModelWithoutChildren():
    model = searchableModel()
    model.searchableItems = lambda: []
    assert model.searchOccurrences("foo", [1]) == []


def test_searchableModelWithChildren():
    model = searchableModel()
    model.searchableItems = lambda: [
        searchableItemMock("R-1"),
        searchableItemMock("R-2")
    ]
    assert model.searchOccurrences("foo", [1]) == [
        "(R-1, foo, [1])",
        "(R-2, foo, [1])",
    ]
