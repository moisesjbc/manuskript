#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.ui.searchMenu import searchMenu
from manuskript.enums import Outline, Character, FlatData


def trigger_filter(filter_key, actions):
    list(filter(lambda action: action.data() == filter_key, actions))[0].trigger()


def test_search_menu_default_columns():
    """
    By default all model columns are selected.
    """
    search_menu = searchMenu()

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


def test_search_menu_no_columns():
    """
    When deselecting "All" filter, no filter is selected by default
    """
    search_menu = searchMenu()

    trigger_filter("All", search_menu.actions())

    assert set(search_menu.columns("Outline")) == set()
    assert set(search_menu.columns("Character")) == set()
    assert set(search_menu.columns("FlatData")) == set()


def test_search_menu_some_columns():
    """
    When deselecting "All" filter and selecting some filters only the columns associated to those filters are enabled.
    """
    search_menu = searchMenu()

    trigger_filter("All", search_menu.actions())
    trigger_filter("OutlineNotes", search_menu.actions())
    trigger_filter("CharacterGoal", search_menu.actions())
    trigger_filter("CharacterNotes", search_menu.actions())
    trigger_filter("FlatDataSummarySentence", search_menu.actions())

    assert set(search_menu.columns("Outline")) == {Outline.notes}
    assert set(search_menu.columns("Character")) == {Character.goal, Character.notes}
    assert set(search_menu.columns("FlatData")) == {FlatData.summarySentence}
