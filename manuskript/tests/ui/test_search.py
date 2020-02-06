#!/usr/bin/env python
# --!-- coding: utf8 --!--

"""Tests for functions"""

import re
import pytest
from manuskript.ui.search import search
from manuskript.enums import SearchOption, SearchModel, Outline, Character, World
from manuskript.functions import mainWindow


@pytest.fixture
def searchWidget():
    return search()


def test_prepareRegexDefault(searchWidget):
    searchWidget.searchMenu.options = lambda: []
    assert searchWidget.prepareRegex("foo") == re.compile("foo", re.UNICODE | re.IGNORECASE)


def test_prepareRegexCaseSensitive(searchWidget):
    searchWidget.searchMenu.options = lambda: [SearchOption.caseSensitive]
    assert searchWidget.prepareRegex("foo") == re.compile("foo", re.UNICODE)

def test_prepareRegexMatchWords(searchWidget):
    searchWidget.searchMenu.options = lambda: [SearchOption.matchWords]
    assert searchWidget.prepareRegex("foo") == re.compile(r"\bfoo\b", re.UNICODE | re.IGNORECASE)


def test_prepareRegexCaseSensitiveandMatchWords(searchWidget):
    searchWidget.searchMenu.options = lambda: [SearchOption.caseSensitive, SearchOption.matchWords]
    assert searchWidget.prepareRegex("foo") == re.compile(r"\bfoo\b", re.UNICODE)


def generateSearchOccurrencesMock(modelType):
    method = lambda regex, columns: ["%s-%s-%s" % (str(modelType), str(regex), ','.join(str(c) for c in columns))]
    return method


def test_searchConcatenatesModelResults():
    searchWidget = search()

    # Mock searchWidget.searchMenu.columns(modelType) so it returns columnsMap[modelType]
    columnsMap = {
        SearchModel.outline: [Outline.title, Outline.summaryFull],
        SearchModel.character: [Character.name, Character.epiphany],
        SearchModel.world: [World.name, World.description]
    }
    searchWidget.searchMenu.columns = lambda modelType: columnsMap.get(modelType, [])

    # Mock searchOccurrences for multiple model classes
    mw = mainWindow()
    mw.loadEmptyDatas()
    mw.mdlOutline.searchOccurrences = generateSearchOccurrencesMock(SearchModel.outline)
    mw.mdlCharacter.searchOccurrences = generateSearchOccurrencesMock(SearchModel.character)
    mw.mdlWorld.searchOccurrences = generateSearchOccurrencesMock(SearchModel.world)

    # Mock method for retrieving search text
    searchWidget.searchTextInput.text = lambda: "foo"

    # Mock method for generating results list so it simply retrieves results
    searchWidgetResults = []
    def collectResults(results):
        nonlocal searchWidgetResults
        searchWidgetResults = results
    searchWidget.generateResultsLists = collectResults

    searchWidget.search()

    assert searchWidgetResults == [
        "SearchModel.outline-re.compile('foo')-Outline.title,Outline.summaryFull",
        "SearchModel.character-re.compile('foo')-Character.name,Character.epiphany",
        "SearchModel.world-re.compile('foo')-World.name,World.description",
    ]
