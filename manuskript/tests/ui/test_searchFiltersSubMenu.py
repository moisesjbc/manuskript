#!/usr/bin/env python
# --!-- coding: utf8 --!--

import pytest
from manuskript.ui.searchFiltersSubMenu import searchFiltersSubMenu
from manuskript.enums import Outline


def trigger_filter(column, actions):
    list(filter(lambda action: action.data() == column, actions))[0].trigger()


MENU_TITLE = "All"
MENU_ELEMENTS = [
    ("Title", Outline.title),
    ("Text", Outline.text),
    ("Notes", Outline.notes)
]


@pytest.fixture
def filters_submenu_all_selected():
    return searchFiltersSubMenu(MENU_TITLE, True, MENU_ELEMENTS)


def test_filters_submenu_title(filters_submenu_all_selected):
    assert filters_submenu_all_selected.actions()[0].text() == filters_submenu_all_selected.tr(MENU_TITLE)


def test_filters_submenu_menu_contains_given_items(filters_submenu_all_selected):
    actions = filters_submenu_all_selected.filterActions()
    print([action.text() for action in actions])
    assert len(actions) == len(MENU_ELEMENTS)
    for i in range(0, len(MENU_ELEMENTS)):
        assert actions[i].text() == filters_submenu_all_selected.tr(MENU_ELEMENTS[i][0])
        assert actions[i].data() == MENU_ELEMENTS[i][1]


def test_filters_submenu_columns_returns_all(filters_submenu_all_selected):
    assert filters_submenu_all_selected.columns() == [Outline.title, Outline.text, Outline.notes]


def test_filters_submenu_all_action_is_checked(filters_submenu_all_selected):
    assert filters_submenu_all_selected.allAction().isChecked() is True


def test_filters_submenu_deselect_action(filters_submenu_all_selected):
    # Deselect one option. "All" option should be disabled.
    trigger_filter(Outline.text, filters_submenu_all_selected.actions())
    assert filters_submenu_all_selected.allAction().isChecked() is False
    assert filters_submenu_all_selected.columns() == [Outline.title, Outline.notes]

    # Select that option again. "All" option should be disabled.
    trigger_filter(Outline.text, filters_submenu_all_selected.actions())
    assert filters_submenu_all_selected.allAction().isChecked() is True


def test_deselect_all(filters_submenu_all_selected):
    filters_submenu_all_selected.allAction().trigger()

    assert filters_submenu_all_selected.allAction().isChecked() is False
    for action in filters_submenu_all_selected.filterActions():
        assert not action.isChecked()


@pytest.fixture
def filters_submenu_none_selected():
    return searchFiltersSubMenu(MENU_TITLE, False, MENU_ELEMENTS)


def test_filters_submenu_columns_returns_none(filters_submenu_none_selected):
    assert filters_submenu_none_selected.columns() == []


def test_filters_submenu_all_action_is_not_checked(filters_submenu_none_selected):
    assert filters_submenu_none_selected.allAction().isChecked() is False


def test_filters_submenu_select_all_options(filters_submenu_none_selected):
    assert filters_submenu_none_selected.allAction().isChecked() is False

    for _, column in MENU_ELEMENTS:
        trigger_filter(column, filters_submenu_none_selected.actions())

    assert filters_submenu_none_selected.allAction().isChecked() is True


def test_filters_submenu_deselect_all(filters_submenu_none_selected):
    filters_submenu_none_selected.allAction().trigger()

    assert filters_submenu_none_selected.allAction().isChecked() is True
    for action in filters_submenu_none_selected.filterActions():
        assert action.isChecked()
