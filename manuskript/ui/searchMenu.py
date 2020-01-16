#!/usr/bin/env python
# --!-- coding: utf8 --!--
from PyQt5.QtWidgets import QMenu, QAction

from manuskript.enums import Outline, Character, FlatData, SearchOption
from manuskript.ui.searchFiltersSubMenu import searchFiltersSubMenu


class searchMenu(QMenu):
    def __init__(self, parent=None):
        QMenu.__init__(self, parent)

        self._filter_actions = {}
        self._option_actions = []

        self._add_section_header("Search in:")
        self._add_outline_filters()
        self._add_character_filters()
        self._add_flat_data_filters()
        self.addSeparator()

        self._add_options()

    def _add_filters_submenu(self, title, filters_info):
        action = QAction(self.tr(title), self)

        action.setMenu(searchFiltersSubMenu("All", True, filters_info))

        self._filter_actions[title] = action
        self.addAction(action)

    def _add_outline_filters(self):
        self._add_filters_submenu("Outline", [
            ("Title", Outline.title),
            ("Text", Outline.text),
            ("Summary (sentence)", Outline.summarySentence),
            ("Summary (full)", Outline.summaryFull),
            ("Notes", Outline.notes),
            ("POV", Outline.POV),
            ("Status", Outline.status),
            ("Label", Outline.label)
        ])

    def _add_character_filters(self):
        self._add_filters_submenu("Character", [
            ("Motivation", Character.motivation),
            ("Goal", Character.goal),
            ("Conflict", Character.conflict),
            ("Epiphany", Character.epiphany),
            ("Summary sentence", Character.summarySentence),
            ("Summary paragraph", Character.summaryPara),
            ("Summary full", Character.summaryFull),
            ("Detailed info", Character.infos),
            ("Notes", Character.notes),
        ])

    def _add_flat_data_filters(self):
        self._add_filters_submenu("FlatData", [
            ("Summary situation", FlatData.summarySituation),
            ("Summary sentence", FlatData.summarySentence),
            ("Summary paragraph", FlatData.summaryPara),
            ("Summary page", FlatData.summaryPage),
            ("Summary full", FlatData.summaryFull)
        ])

    def _add_options(self):
        options = [
            ("Case sensitive", True, SearchOption.caseSensitive),
            ("Match words", False, SearchOption.matchWords)
        ]

        self._add_section_header("Options")

        for title, checked, option in options:
            a = QAction(title, self)
            a.setCheckable(True)
            a.setChecked(checked)
            a.setData(option)
            self._option_actions.append(a)
            self.addAction(a)

    def _add_section_header(self, title):
        action = QAction(self.tr(title), self)
        action.setEnabled(False)
        self.addAction(action)
        self.addSeparator()

    def columns(self, model_prefix):
        return self._filter_actions[model_prefix].menu().columns()

    def options(self):
        options = []

        for option_action in self._option_actions:
            if option_action.isChecked():
                options.append(option_action.data())

        return options
