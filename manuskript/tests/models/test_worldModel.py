#!/usr/bin/env python
# --!-- coding: utf8 --!--

"""Tests for worldModel"""

import re
import pytest
from manuskript.enums import World
from manuskript.models.worldModel import worldModel
from PyQt5.Qt import QStandardItem
from manuskript.models.searchResult import searchResult
from manuskript.enums import SearchModel

SEARCH_REGEX = re.compile("foo")
WORLD_ID = "13"
WORLD_NAME = ("World foo", [(6, 9)])
WORLD_DESCRIPTION = ("This plot description is full of foo", [(33, 36)])
WORLD_PASSION = ("foo is a good passion", [(0, 3)])
WORLD_CONFLICT = ("There are a lot of conflicts for foo", [(33, 36)])
WORLD_CHILD_ID = "15"
WORLD_CHILD_NAME = ("World child is also foo", [(20, 23)])


@pytest.fixture
def world():
    # Build a World with all the test data.
    world = worldModel(None)
    world.setItem(0, World.ID, QStandardItem(WORLD_ID))
    world.setItem(0, World.name, QStandardItem(WORLD_NAME[0]))
    world.setItem(0, World.description, QStandardItem(WORLD_DESCRIPTION[0]))
    world.setItem(0, World.passion, QStandardItem(WORLD_PASSION[0]))
    world.setItem(0, World.conflict, QStandardItem(WORLD_CONFLICT[0]))

    world.itemByID(WORLD_ID).appendRow([
        QStandardItem(WORLD_CHILD_NAME[0]),
        QStandardItem(WORLD_CHILD_ID)
    ])

    return world


def test_searchInName(world):
    assert world.searchOccurrences(SEARCH_REGEX, [World.name]) == \
           [searchResult(SearchModel.world, WORLD_ID, World.name, WORLD_NAME[0], "", WORLD_NAME[1][0])] + \
           [searchResult(SearchModel.world, WORLD_CHILD_ID, World.name, WORLD_CHILD_NAME[0], WORLD_NAME[0], WORLD_CHILD_NAME[1][0])]


def test_searchInDescription(world):
    assert world.searchOccurrences(SEARCH_REGEX, [World.description]) == \
           [searchResult(SearchModel.world, WORLD_ID, World.description, WORLD_NAME[0], "", WORLD_DESCRIPTION[1][0])]


def test_searchInPassion(world):
    assert world.searchOccurrences(SEARCH_REGEX, [World.passion]) == \
           [searchResult(SearchModel.world, WORLD_ID, World.passion, WORLD_NAME[0], "", WORLD_PASSION[1][0])]


def test_searchInConflict(world):
    assert world.searchOccurrences(SEARCH_REGEX, [World.conflict]) == \
           [searchResult(SearchModel.world, WORLD_ID, World.conflict, WORLD_NAME[0], "", WORLD_CONFLICT[1][0])]
