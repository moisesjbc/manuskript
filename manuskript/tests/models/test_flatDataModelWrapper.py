#!/usr/bin/env python
# --!-- coding: utf8 --!--

"""Tests for flatDataModelWrapper"""

from manuskript.models.flatDataModelWrapper import flatDataModelWrapper as FlatDataModelWrapper
from manuskript.models.searchResult import searchResult
from manuskript.enums import FlatData, SearchModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import re
import pytest

SEARCH_REGEX = re.compile("foo")

TEST_DATA = {
    FlatData.summarySituation: ("Situation is foo", [
        searchResult(SearchModel.flatData,
                     None,
                     FlatData.summarySituation,
                     QStandardItemModel().tr("Situation"),
                     QStandardItemModel().tr("Summary"),
                     (13, 16))
    ]),
    FlatData.summarySentence: ("In one sentence: foo is foo", [
        searchResult(SearchModel.flatData,
                     None,
                     FlatData.summarySentence,
                     QStandardItemModel().tr("One sentence summary"),
                     QStandardItemModel().tr("Summary"),
                     (17, 20)),
        searchResult(SearchModel.flatData,
                     None,
                     FlatData.summarySentence,
                     QStandardItemModel().tr("One sentence summary"),
                     QStandardItemModel().tr("Summary"),
                     (24, 27))
    ]),
    FlatData.summaryPara: ("foo for paragraph", [
        searchResult(SearchModel.flatData,
                     None,
                     FlatData.summaryPara,
                     QStandardItemModel().tr("One paragraph summary"),
                     QStandardItemModel().tr("Summary"),
                     (0, 3))
    ]),
    FlatData.summaryPage: ("One page and foo", [
        searchResult(SearchModel.flatData,
                     None,
                     FlatData.summaryPage,
                     QStandardItemModel().tr("One page summary"),
                     QStandardItemModel().tr("Summary"),
                     (13, 16))
    ]),
    FlatData.summaryFull: ("Full of foo", [
        searchResult(SearchModel.flatData,
                     None,
                     FlatData.summaryFull,
                     QStandardItemModel().tr("Full summary"),
                     QStandardItemModel().tr("Summary"),
                     (8, 11))
    ])
}


@pytest.fixture
def flatDataModelWrapper():
    qStandardItemModel = QStandardItemModel()
    qStandardItemModel.appendRow([])
    qStandardItemModel.appendRow([QStandardItem(text) for text in [
        TEST_DATA[FlatData.summarySituation][0],
        TEST_DATA[FlatData.summarySentence][0],
        TEST_DATA[FlatData.summaryPara][0],
        TEST_DATA[FlatData.summaryPage][0],
        TEST_DATA[FlatData.summaryFull][0]
    ]])
    return FlatDataModelWrapper(qStandardItemModel, qStandardItemModel.tr)


def test_characterSearchOccurrencesInSituation(flatDataModelWrapper):
    assert flatDataModelWrapper.searchOccurrences(SEARCH_REGEX, [FlatData.summarySituation]) == TEST_DATA[FlatData.summarySituation][1]


def test_characterSearchOccurrencesInSituationAndSentence(flatDataModelWrapper):
    assert flatDataModelWrapper.searchOccurrences(SEARCH_REGEX, [FlatData.summarySituation, FlatData.summarySentence]) == \
           TEST_DATA[FlatData.summarySituation][1] + TEST_DATA[FlatData.summarySentence][1]


def test_characterSearchOccurrencesInParaSummary(flatDataModelWrapper):
    assert flatDataModelWrapper.searchOccurrences(SEARCH_REGEX, [FlatData.summaryPara]) == \
           TEST_DATA[FlatData.summaryPara][1]


def test_characterSearchOccurrencesInPageSummary(flatDataModelWrapper):
    assert flatDataModelWrapper.searchOccurrences(SEARCH_REGEX, [FlatData.summaryPage]) == \
           TEST_DATA[FlatData.summaryPage][1]

def test_characterSearchOccurrencesInFullSummary(flatDataModelWrapper):
    assert flatDataModelWrapper.searchOccurrences(SEARCH_REGEX, [FlatData.summaryFull]) == \
           TEST_DATA[FlatData.summaryFull][1]