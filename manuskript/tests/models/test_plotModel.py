#!/usr/bin/env python
# --!-- coding: utf8 --!--

"""Tests for plotModel"""

import re
import pytest
from manuskript.enums import Plot, PlotStep
from manuskript.functions import mainWindow
from manuskript.models.characterModel import Character, characterModel
from manuskript.models.plotModel import plotModel
from PyQt5.Qt import QStandardItem
from manuskript.models.searchResult import searchResult
from manuskript.enums import SearchModel

SEARCH_REGEX = re.compile("foo")
PLOT_ID = "13"
PLOT_NAME = ("Plot foo", [(5, 8)])
PLOT_CHARACTERS_IDS = ["1", "2", "3"]
PLOT_CHARACTERS = [
    ("1", "foo the great", [(0, 0)]),
    ("2", "Jacob", []),
    ("3", "foo the not-so-great", [(2, 2)])
]
PLOT_IMPORTANCE = "0"
PLOT_DESCRIPTION = ("This plot description is full of foo", [(33, 36)])
PLOT_RESULT = ("foo is a good result", [(0, 3)])
PLOT_SUMMARY = ("As summarized: foo is good", [(15, 18)])

PLOT_STEP_1_NAME = ("Subplot foo 1", [(8, 11)])
PLOT_STEP_2_NAME = ("Subplot 2", [])
PLOT_STEP_2_SUMMARY = ("Subplot summary is foo", [(19, 22)])


def getCharacterByIDMock(characterID):
    for id, name, _ in PLOT_CHARACTERS:
        if id == characterID:
            return Character(characterModel(None), name)


@pytest.fixture
def plot():
    # On construction plotModel tries to access self.mw.mdlCharacter.rowCount(), which is undefined unless we call
    # mainWindow().loadEmptyDatas()
    mainWindow().loadEmptyDatas()

    # Build a Plot with all the test data.
    plot = plotModel(None)
    mainWindow().lstPlots.setPlotModel(plot)
    plot.setItem(0, Plot.ID, QStandardItem(PLOT_ID))
    plot.setItem(0, Plot.name, QStandardItem(PLOT_NAME[0]))
    plot.setItem(0, Plot.importance, QStandardItem(PLOT_IMPORTANCE))
    plot.setItem(0, Plot.characters, QStandardItem())
    plot.setItem(0, Plot.description, QStandardItem(PLOT_DESCRIPTION[0]))
    plot.setItem(0, Plot.result, QStandardItem(PLOT_RESULT[0]))
    plot.setItem(0, Plot.summary, QStandardItem(PLOT_SUMMARY[0]))

    plot.setItem(0, Plot.steps, QStandardItem())
    plot.item(0, Plot.steps).appendRow([
        QStandardItem(PLOT_STEP_1_NAME[0]),
        QStandardItem("1"),
        QStandardItem(),
        QStandardItem()
    ])
    plot.item(0, Plot.steps).appendRow([
        QStandardItem(PLOT_STEP_2_NAME[0]),
        QStandardItem("2"),
        QStandardItem(),
        QStandardItem(PLOT_STEP_2_SUMMARY[0])
    ])

    # Populate plot with character IDs and mock method for returning te associated characters.
    mainWindow().mdlCharacter.getCharacterByID = getCharacterByIDMock
    for characterId, characterName, _ in PLOT_CHARACTERS:
        plot.item(0, Plot.characters).appendRow(QStandardItem(characterId))

    return plot


def test_searchInName(plot):
    assert plot.searchOccurrences(SEARCH_REGEX, [Plot.name]) == \
           [searchResult(SearchModel.plot, PLOT_ID, Plot.name, PLOT_NAME[0], "", PLOT_NAME[1][0])]


def test_searchInCharacters(plot):
    assert plot.searchOccurrences(SEARCH_REGEX, [Plot.characters]) == \
           [searchResult(SearchModel.plot, PLOT_ID, Plot.characters, PLOT_NAME[0], "", PLOT_CHARACTERS[0][2][0])] + \
            [searchResult(SearchModel.plot, PLOT_ID, Plot.characters, PLOT_NAME[0], "", PLOT_CHARACTERS[2][2][0])]


def test_searchInDescription(plot):
    assert plot.searchOccurrences(SEARCH_REGEX, [Plot.description]) == \
           [searchResult(SearchModel.plot, PLOT_ID, Plot.description, PLOT_NAME[0], "", PLOT_DESCRIPTION[1][0])]


def test_searchInResult(plot):
    assert plot.searchOccurrences(SEARCH_REGEX, [Plot.result]) == \
           [searchResult(SearchModel.plot, PLOT_ID, Plot.result, PLOT_NAME[0], "", PLOT_RESULT[1][0])]


def test_searchInSummary(plot):
    assert plot.searchOccurrences(SEARCH_REGEX, [Plot.summary]) == \
           [searchResult(SearchModel.plot, PLOT_ID, Plot.summary, PLOT_NAME[0], "", PLOT_SUMMARY[1][0])]


def test_searchInPlotStep1(plot):
    assert plot.searchOccurrences(SEARCH_REGEX, [Plot.steps]) == \
           [searchResult(SearchModel.plotStep, (PLOT_ID, 0), PlotStep.name, PLOT_STEP_1_NAME[0], PLOT_NAME[0],
                         PLOT_STEP_1_NAME[1][0])] + \
           [searchResult(SearchModel.plotStep, (PLOT_ID, 1), PlotStep.summary, PLOT_STEP_2_NAME[0], PLOT_NAME[0],
                         PLOT_STEP_2_SUMMARY[1][0])]
