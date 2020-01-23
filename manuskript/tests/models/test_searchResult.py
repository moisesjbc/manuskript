#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.models.searchResult import searchResult
from manuskript.enums import Character


def test_searchResultConstructionOk():
    result = searchResult("Character", "3", Character.notes, "Lucas", "A > B > C", (15, 18))
    assert result.id() == "3"
    assert result.column() == Character.notes
    assert result.title() == "Lucas"
    assert result.path() == "A > B > C"
    assert result.pos() == (15, 18)

