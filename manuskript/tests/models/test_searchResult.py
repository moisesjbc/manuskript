#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.models.searchResult import searchResult
from manuskript.enums import Character


def test_searchResult_construction_ok():
    search_result = searchResult("Character", "3", Character.notes, "Lucas", "A > B > C", (15, 18))
    assert search_result.id() == "3"
    assert search_result.column() == Character.notes
    assert search_result.title() == "Lucas"
    assert search_result.path() == "A > B > C"
    assert search_result.pos() == (15, 18)

