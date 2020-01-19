#!/usr/bin/env python
# --!-- coding: utf8 --!--

import pytest
from manuskript.ui.searchMenu import searchMenu
from manuskript.enums import Outline, Character, FlatData, World, SearchOption, Plot


def trigger_filter(filter_key, actions):
    list(filter(lambda action: action.data() == filter_key, actions))[0].trigger()


@pytest.fixture
def search_menu():
    return searchMenu()


def test_search_menu_actions(search_menu):
    assert [action.text() for action in search_menu.actions()] == [
        search_menu.tr("Search in:"),
        '',
        search_menu.tr("Character"),
        search_menu.tr("FlatData"),
        search_menu.tr("Outline"),
        search_menu.tr("Plot"),
        search_menu.tr("World"),
        '',
        search_menu.tr("Options"),
        '',
        search_menu.tr("Case sensitive"),
        search_menu.tr("Match words")
    ]


def test_search_menu_default_columns(search_menu):
    """
    By default all model columns are selected.
    """
    assert set(search_menu.columns("Outline")) == {
        Outline.title, Outline.text, Outline.summaryFull,
        Outline.summarySentence, Outline.notes, Outline.POV,
        Outline.status, Outline.label
    }

    assert set(search_menu.columns("Character")) == {
        Character.motivation, Character.goal, Character.conflict,
        Character.epiphany, Character.summarySentence, Character.summaryPara,
        Character.summaryFull, Character.infos, Character.notes
    }

    assert set(search_menu.columns("FlatData")) == {
        FlatData.summarySituation, FlatData.summarySentence, FlatData.summaryPara,
        FlatData.summaryPage, FlatData.summaryFull
    }

    assert set(search_menu.columns("World")) == {
        World.name, World.description, World.passion, World.conflict
    }

    assert set(search_menu.columns("Plot")) == {
        Plot.name, Plot.characters, Plot.description, Plot.result, Plot.steps
    }


def test_search_menu_default_options(search_menu):
    assert search_menu.options() == [SearchOption.caseSensitive]

"""
def test_search_menu_no_columns():
    ""
    When deselecting "All" filter, no filter is selected by default
    ""
    search_menu = searchMenu()

    trigger_filter("All", search_menu.actions())

    assert set(search_menu.columns("Outline")) == set()
    assert set(search_menu.columns("Character")) == set()
    assert set(search_menu.columns("FlatData")) == set()


def test_search_menu_some_columns():
    ""
    When deselecting "All" filter and selecting some filters only the columns associated to those filters are enabled.
    ""
    search_menu = searchMenu()

    trigger_filter("All", search_menu.actions())
    trigger_filter("OutlineNotes", search_menu.actions())
    trigger_filter("CharacterGoal", search_menu.actions())
    trigger_filter("CharacterNotes", search_menu.actions())
    trigger_filter("FlatDataSummarySentence", search_menu.actions())

    assert set(search_menu.columns("Outline")) == {Outline.notes}
    assert set(search_menu.columns("Character")) == {Character.goal, Character.notes}
    assert set(search_menu.columns("FlatData")) == {FlatData.summarySentence}
"""