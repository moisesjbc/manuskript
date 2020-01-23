#!/usr/bin/env python
# --!-- coding: utf8 --!--

import pytest
from manuskript.ui.searchFiltersSubMenu import searchFiltersSubMenu
from manuskript.enums import Outline


def triggerFilter(columns, actions):
    list(filter(lambda action: action.data() == columns, actions))[0].trigger()


MENU_TITLE = "All"
MENU_ELEMENTS = [
    ("Title", [Outline.title]),
    ("Text", [Outline.text]),
    ("Notes", [Outline.notes]),
    ("Summaries", [Outline.summarySentence, Outline.summaryFull])
]


@pytest.fixture
def filtersSubmenuAllSelected():
    return searchFiltersSubMenu(MENU_TITLE, True, MENU_ELEMENTS)


def test_filtersSubmenuTitle(filtersSubmenuAllSelected):
    assert filtersSubmenuAllSelected.actions()[0].text() == filtersSubmenuAllSelected.tr(MENU_TITLE)


def test_filtersSubmenuMenuContainsGivenItems(filtersSubmenuAllSelected):
    actions = filtersSubmenuAllSelected.filterActions()
    print([action.text() for action in actions])
    assert len(actions) == len(MENU_ELEMENTS)
    for i in range(0, len(MENU_ELEMENTS)):
        assert actions[i].text() == filtersSubmenuAllSelected.tr(MENU_ELEMENTS[i][0])
        assert actions[i].data() == MENU_ELEMENTS[i][1]


def test_filtersSubmenuColumnsReturnsAll(filtersSubmenuAllSelected):
    assert filtersSubmenuAllSelected.columns() == [Outline.title, Outline.text, Outline.notes,
                                                   Outline.summarySentence, Outline.summaryFull]


def test_filtersSubmenuAllActionIsChecked(filtersSubmenuAllSelected):
    assert filtersSubmenuAllSelected.allAction().isChecked() is True


def test_filtersSubmenuDeselectAction(filtersSubmenuAllSelected):
    # Deselect one option. "All" option should be disabled.
    triggerFilter([Outline.text], filtersSubmenuAllSelected.actions())
    assert filtersSubmenuAllSelected.allAction().isChecked() is False
    assert filtersSubmenuAllSelected.columns() == [Outline.title, Outline.notes, Outline.summarySentence,
                                                   Outline.summaryFull]

    # Select that option again. "All" option should be disabled.
    triggerFilter([Outline.text], filtersSubmenuAllSelected.actions())
    assert filtersSubmenuAllSelected.allAction().isChecked() is True


def test_deselectAll(filtersSubmenuAllSelected):
    filtersSubmenuAllSelected.allAction().trigger()

    assert filtersSubmenuAllSelected.allAction().isChecked() is False
    for action in filtersSubmenuAllSelected.filterActions():
        assert not action.isChecked()


@pytest.fixture
def filtersSubmenuNoneSelected():
    return searchFiltersSubMenu(MENU_TITLE, False, MENU_ELEMENTS)


def test_filtersSubmenuColumnsReturnsNone(filtersSubmenuNoneSelected):
    assert filtersSubmenuNoneSelected.columns() == []


def test_filtersSubmenuAllActionIsNotChecked(filtersSubmenuNoneSelected):
    assert filtersSubmenuNoneSelected.allAction().isChecked() is False


def test_filtersSubmenuSelectAllOptions(filtersSubmenuNoneSelected):
    assert filtersSubmenuNoneSelected.allAction().isChecked() is False

    for _, column in MENU_ELEMENTS:
        triggerFilter(column, filtersSubmenuNoneSelected.actions())

    assert filtersSubmenuNoneSelected.allAction().isChecked() is True


def test_filtersSubmenuDeselectAll(filtersSubmenuNoneSelected):
    filtersSubmenuNoneSelected.allAction().trigger()

    assert filtersSubmenuNoneSelected.allAction().isChecked() is True
    for action in filtersSubmenuNoneSelected.filterActions():
        assert action.isChecked()
