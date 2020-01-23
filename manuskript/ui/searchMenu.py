#!/usr/bin/env python
# --!-- coding: utf8 --!--
from PyQt5.QtWidgets import QMenu, QAction

from manuskript.enums import Outline, Character, FlatData, World, Plot, SearchOption
from manuskript.ui.searchFiltersSubMenu import searchFiltersSubMenu


class searchMenu(QMenu):
    def __init__(self, parent=None):
        QMenu.__init__(self, parent)

        self._filter_actions = {}
        self._optionActions = []

        self._addSectionHeader("Search in:")
        self._addCharacterFilters()
        self._addFlatDataFilters()
        self._addOutlineFilters()
        self._addPlotFilters()
        self._addWorldFilters()
        self.addSeparator()

        self._addOptions()

    def _add_filters_submenu(self, title, filters_info):
        action = QAction(self.tr(title), self)

        action.setMenu(searchFiltersSubMenu("All", True, filters_info))

        self._filter_actions[title] = action
        self.addAction(action)

    def _addOutlineFilters(self):
        self._add_filters_submenu("Outline", [
            ("Title", [Outline.title]),
            ("Text", [Outline.text]),
            ("Summary (sentence)", [Outline.summarySentence]),
            ("Summary (full)", [Outline.summaryFull]),
            ("Notes", [Outline.notes]),
            ("POV", [Outline.POV]),
            ("Status", [Outline.status]),
            ("Label", [Outline.label])
        ])

    def _addCharacterFilters(self):
        self._add_filters_submenu("Character", [
            ("Motivation", [Character.motivation]),
            ("Goal", [Character.goal]),
            ("Conflict", [Character.conflict]),
            ("Epiphany", [Character.epiphany]),
            ("Summary sentence", [Character.summarySentence]),
            ("Summary paragraph", [Character.summaryPara]),
            ("Summary full", [Character.summaryFull]),
            ("Detailed info", [Character.infos]),
            ("Notes", [Character.notes]),
        ])

    def _addFlatDataFilters(self):
        self._add_filters_submenu("FlatData", [
            ("Summary situation", [FlatData.summarySituation]),
            ("Summary sentence", [FlatData.summarySentence]),
            ("Summary paragraph", [FlatData.summaryPara]),
            ("Summary page", [FlatData.summaryPage]),
            ("Summary full", [FlatData.summaryFull])
        ])

    def _addPlotFilters(self):
        self._add_filters_submenu("Plot", [
            ("Name", [Plot.name]),
            ("Characters", [Plot.characters]),
            ("Description", [Plot.description]),
            ("Result", [Plot.result]),
            ("Steps", [Plot.steps])
        ])

    def _addWorldFilters(self):
        self._add_filters_submenu("World", [
            ("Name", [World.name]),
            ("Description", [World.description]),
            ("Passion", [World.passion]),
            ("Conflict", [World.conflict])
        ])

    def _addOptions(self):
        options = [
            ("Case sensitive", True, SearchOption.caseSensitive),
            ("Match words", False, SearchOption.matchWords),
            ("Regex", False, SearchOption.regex)
        ]

        self._addSectionHeader("Options")

        for title, checked, option in options:
            a = QAction(title, self)
            a.setCheckable(True)
            a.setChecked(checked)
            a.setData(option)
            self._optionActions.append(a)
            self.addAction(a)

    def _addSectionHeader(self, title):
        action = QAction(self.tr(title), self)
        action.setEnabled(False)
        self.addAction(action)
        self.addSeparator()

    def columns(self, modelPrefix):
        return self._filter_actions[modelPrefix].menu().columns()

    def options(self):
        options = []

        for optionAction in self._optionActions:
            if optionAction.isChecked():
                options.append(optionAction.data())

        return options
