#!/usr/bin/env python
# --!-- coding: utf8 --!--

import pytest
from manuskript.models.searchResult import searchResult
from manuskript.enums import Character, SearchModel


@pytest.fixture
def result():
    return searchResult(SearchModel.character, "3", Character.notes, "Lucas", "A > B > C", (15, 18))


def test_searchResultConstructionOk(result):
    assert result.id() == "3"
    assert result.column() == Character.notes
    assert result.title() == "Lucas"
    assert result.path() == "A > B > C"
    assert result.pos() == (15, 18)


def test_searchResultRepr(result):
    assert str(result) == "(SearchModel.character, 3, Character.notes, Lucas, A > B > C, (15, 18))"
