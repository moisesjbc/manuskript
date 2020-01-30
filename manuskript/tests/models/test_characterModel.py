#!/usr/bin/env python
# --!-- coding: utf8 --!--

"""Tests for characterModel"""

from manuskript.models.characterModel import Character, characterModel, CharacterInfo
from manuskript.models.searchResult import searchResult
from manuskript.enums import Character as C, SearchModel
import re
import pytest

CHARACTER_ID = "13"
CHARACTER_NAME = "character"
CHARACTER_MOTIVATION = "Character motivation"
CHARACTER_GOAL = "Character goal"
CHARACTER_CONFLICT = "Character conflict"
CHARACTER_EPIPHANY = "Character epiphany"
CHARACTER_SUMMARY_SENTENCE = "Character summary sentence"
CHARACTER_SUMMARY_PARAGRAPH = "Character summary paragraph"
CHARACTER_SUMMARY_FULL = "Character summary full with value"
CHARACTER_NOTES = "Character notes"
CHARACTER_INFOS = [("info1-var", "value")]


@pytest.fixture
def character():
    character = Character(characterModel(None), CHARACTER_NAME)

    character._data[C.ID] = CHARACTER_ID
    character._data[C.motivation] = CHARACTER_MOTIVATION
    character._data[C.goal] = CHARACTER_GOAL
    character._data[C.conflict] = CHARACTER_CONFLICT
    character._data[C.epiphany] = CHARACTER_EPIPHANY
    character._data[C.summarySentence] = CHARACTER_SUMMARY_SENTENCE
    character._data[C.summaryPara] = CHARACTER_SUMMARY_PARAGRAPH
    character._data[C.summaryFull] = CHARACTER_SUMMARY_FULL
    character._data[C.notes] = CHARACTER_NOTES
    character.infos = CHARACTER_INFOS

    return character


def test_characterSearchData(character):
    assert character.searchData(C.name) == CHARACTER_NAME
    assert character.searchData(C.motivation) == CHARACTER_MOTIVATION
    assert character.searchData(C.goal) == CHARACTER_GOAL
    assert character.searchData(C.conflict) == CHARACTER_CONFLICT
    assert character.searchData(C.epiphany) == CHARACTER_EPIPHANY
    assert character.searchData(C.summarySentence) == CHARACTER_SUMMARY_SENTENCE
    assert character.searchData(C.summaryPara) == CHARACTER_SUMMARY_PARAGRAPH
    assert character.searchData(C.summaryFull) == CHARACTER_SUMMARY_FULL
    assert character.searchData(C.notes) == CHARACTER_NOTES
    assert character.searchData(C.infos) == CHARACTER_INFOS


def test_characterSearchName(character):
    assert character.searchTitle() == CHARACTER_NAME


def test_characterSearchOccurrencesInSummaries(character):
    searchRegex = re.compile("summary")
    assert character.searchOccurrences(searchRegex, [C.summarySentence]) == [
        searchResult(SearchModel.character, CHARACTER_ID, C.summarySentence, CHARACTER_NAME, "", (10, 10 + len("summary")))
    ]

    assert character.searchOccurrences(searchRegex, [C.summarySentence, C.summaryFull]) == [
        searchResult(SearchModel.character, CHARACTER_ID, C.summarySentence, CHARACTER_NAME, "",
                     (10, 10 + len("summary"))),
        searchResult(SearchModel.character, CHARACTER_ID, C.summaryFull, CHARACTER_NAME, "",
                     (10, 10 + len("summary")))
    ]

    assert character.searchOccurrences(re.compile("value"), [C.summarySentence, C.summaryFull]) == [
        searchResult(SearchModel.character, CHARACTER_ID, C.summaryFull, CHARACTER_NAME, "",
                     (28, 28 + len("value")))
    ]

def test_characterSearchOccurrencesInInfos(character):
    character.infos = [
        CharacterInfo(character, "var-1", "val-1-foo"),
        CharacterInfo(character, "var-2-foo", "val-2"),
        CharacterInfo(character, "var-3-foo", "val-3-foo")
    ]
    results = character.searchOccurrences(re.compile("foo"), [C.infos])
    assert results == [
        searchResult(SearchModel.character, CHARACTER_ID, C.infos, CHARACTER_NAME, "", (0, 1)),
        searchResult(SearchModel.character, CHARACTER_ID, C.infos, CHARACTER_NAME, "", (1, 0)),
        searchResult(SearchModel.character, CHARACTER_ID, C.infos, CHARACTER_NAME, "", (2, 0)),
        searchResult(SearchModel.character, CHARACTER_ID, C.infos, CHARACTER_NAME, "", (2, 1))
    ]
