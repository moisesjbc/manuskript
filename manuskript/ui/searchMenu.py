#!/usr/bin/env python
# --!-- coding: utf8 --!--
from PyQt5.QtWidgets import QMenu, QAction

from manuskript.enums import Outline, Character, FlatData, World, Plot, SearchOption, SearchModel
from manuskript.ui.searchFiltersSubMenu import searchFiltersSubMenu


class searchMenu(QMenu):
    def __init__(self, parent=None):
        QMenu.__init__(self, parent)

        self._filter_actions = {}
        self._optionActions = []

        self._addSectionHeader(self.tr("Search in:"))
        self._addCharacterFilters()
        self._addFlatDataFilters()
        self._addOutlineFilters()
        self._addPlotFilters()
        self._addWorldFilters()
        self.addSeparator()

        self._addOptions()

    def _add_filters_submenu(self, model, title, filters_info):
        action = QAction(title, self)

        action.setMenu(searchFiltersSubMenu(self.tr("All"), True, filters_info))

        self._filter_actions[model] = action
        self.addAction(action)

    def _addOutlineFilters(self):
        self._add_filters_submenu(SearchModel.outline, self.tr("Outline"), [
            (self.tr("Title"), [Outline.title]),
            (self.tr("Text"), [Outline.text]),
            (self.tr("Summary sentence"), [Outline.summarySentence]),
            (self.tr("Full summary"), [Outline.summaryFull]),
            (self.tr("Notes"), [Outline.notes]),
            (self.tr("POV"), [Outline.POV]),
            (self.tr("Status"), [Outline.status]),
            (self.tr("Label"), [Outline.label])
        ])

    def _addCharacterFilters(self):
        self._add_filters_submenu(SearchModel.character, self.tr("Characters"), [
            (self.tr("Name"), [Character.name]),
            (self.tr("Motivation"), [Character.motivation]),
            (self.tr("Goal"), [Character.goal]),
            (self.tr("Conflict"), [Character.conflict]),
            (self.tr("Epiphany"), [Character.epiphany]),
            (self.tr("Sentence summary"), [Character.summarySentence]),
            (self.tr("Paragraph summary"), [Character.summaryPara]),
            (self.tr("Full summary"), [Character.summaryFull]),
            (self.tr("Detailed info"), [Character.infos]),
            (self.tr("Notes"), [Character.notes]),
        ])

    def _addFlatDataFilters(self):
        self._add_filters_submenu(SearchModel.flatData, self.tr("Flat data"), [
            (self.tr("Situation"), [FlatData.summarySituation]),
            (self.tr("Sentence summary"), [FlatData.summarySentence]),
            (self.tr("Paragraph summary"), [FlatData.summaryPara]),
            (self.tr("Page summary"), [FlatData.summaryPage]),
            (self.tr("Full summary"), [FlatData.summaryFull])
        ])

    def _addPlotFilters(self):
        self._add_filters_submenu(SearchModel.plot, self.tr("Plots"), [
            (self.tr("Name"), [Plot.name]),
            (self.tr("Characters"), [Plot.characters]),
            (self.tr("Description"), [Plot.description]),
            (self.tr("Result"), [Plot.result]),
            (self.tr("Steps"), [Plot.steps])
        ])

    def _addWorldFilters(self):
        self._add_filters_submenu(SearchModel.world, self.tr("World"), [
            (self.tr("Name"), [World.name]),
            (self.tr("Description"), [World.description]),
            (self.tr("Passion"), [World.passion]),
            (self.tr("Conflict"), [World.conflict])
        ])

    def _addOptions(self):
        options = [
            (self.tr("Case sensitive"), True, SearchOption.caseSensitive),
            (self.tr("Match words"), False, SearchOption.matchWords),
            (self.tr("Regex"), False, SearchOption.regex)
        ]

        self._addSectionHeader(self.tr("Options"))

        for title, checked, option in options:
            a = QAction(title, self)
            a.setCheckable(True)
            a.setChecked(checked)
            a.setData(option)
            self._optionActions.append(a)
            self.addAction(a)

    def _addSectionHeader(self, title):
        action = QAction(title, self)
        action.setEnabled(False)
        self.addAction(action)
        self.addSeparator()

    def columns(self, model):
        return self._filter_actions[model].menu().columns()

    def options(self):
        options = []

        for optionAction in self._optionActions:
            if optionAction.isChecked():
                options.append(optionAction.data())

        return options
