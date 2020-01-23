#!/usr/bin/env python
# --!-- coding: utf8 --!--

import pytest
from manuskript.ui.searchMenu import searchMenu
from manuskript.enums import Outline, Character, FlatData, World, SearchOption, Plot


def triggerFilter(filter_key, actions):
    list(filter(lambda action: action.data() == filter_key, actions))[0].trigger()


@pytest.fixture
def search_menu():
    return searchMenu()


def test_searchMenuActions(search_menu):
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


def test_searchMenuDefaultColumns(search_menu):
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


def test_searchMenuDefaultOptions(search_menu):
    assert search_menu.options() == [SearchOption.caseSensitive]
