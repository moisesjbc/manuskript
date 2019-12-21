#!/usr/bin/env python
# --!-- coding: utf8 --!--
from PyQt5.QtWidgets import QMenu, QAction

from manuskript.enums import Outline, Character, FlatData
from manuskript.models.searchFilter import searchFilter


class searchMenu(QMenu):
    def __init__(self, parent=None):
        QMenu.__init__(self, parent)

        self.filters = {
            "All": searchFilter("All", True),
            "OutlineTitle": searchFilter("[Outline] Title", False, Outline.title),
            "OutlineText": searchFilter("[Outline] Text", False, Outline.text),
            "OutlineSummarySentence": searchFilter("[Outline] Summary (sentence)", False, Outline.summarySentence),
            "OutlineSummaryFull": searchFilter("[Outline] Summary (full)", False, Outline.summaryFull),
            "OutlineNotes": searchFilter("[Outline] Notes", False, Outline.notes),
            "OutlinePOV": searchFilter("[Outline] POV", False, Outline.POV),
            "OutlineStatus": searchFilter("[Outline] Status", False, Outline.status),
            "OutlineLabel": searchFilter("[Outline] Label", False, Outline.label),

            "CharacterMotivation": searchFilter("[Character] Motivation", False, Character.motivation),
            "CharacterGoal": searchFilter("[Character] Goal", False, Character.goal),
            "CharacterConflict": searchFilter("[Character] Conflict", False, Character.conflict),
            "CharacterEpiphany": searchFilter("[Character] Epiphany", False, Character.epiphany),
            "CharacterSummarySentence": searchFilter("[Character] Summary sentence", False, Character.summarySentence),
            "CharacterSummaryPara": searchFilter("[Character] Summary paragraph", False, Character.summaryPara),
            "CharacterSummaryFull": searchFilter("[Character] Summary full", False, Character.summaryFull),
            "CharacterInfo": searchFilter("[Character] Detailed info", False, Character.infos),
            "CharacterNotes": searchFilter("[Character] Notes", False, Character.notes),

            "FlatDataSummarySituation": searchFilter("[FlatData] Summary situation", False, FlatData.summarySituation),
            "FlatDataSummarySentence": searchFilter("[FlatData] Summary sentence", False, FlatData.summarySentence),
            "FlatDataSummaryPara": searchFilter("[FlatData] Summary paragraph", False, FlatData.summaryPara),
            "FlatDataSummaryPage": searchFilter("[FlatData] Summary page", False, FlatData.summaryPage),
            "FlatDataSummaryFull": searchFilter("[FlatData] Summary full", False, FlatData.summaryFull)
        }

        self.options = {
            "CS": [self.tr("Case sensitive"), True],
            "MatchWords": [self.tr("Match words"), False]
        }

        self._generate_options()

    def _generate_options(self):
        a = QAction(self.tr("Search in:"), self)
        a.setEnabled(False)
        self.addAction(a)
        for filterKey in self.filters:
            a = QAction(self.tr(self.filters[filterKey].label()), self)
            a.setCheckable(True)
            a.setChecked(self.filters[filterKey].enabled())
            a.setData(filterKey)
            a.triggered.connect(self._update_filters)
            self.addAction(a)
        self.addSeparator()

        a = QAction(self.tr("Options:"), self)
        a.setEnabled(False)
        self.addAction(a)
        for optionKey in self.options:
            a = QAction(self.options[optionKey][0], self)
            a.setCheckable(True)
            a.setChecked(self.options[optionKey][1])
            a.setData(optionKey)
            a.triggered.connect(self._update_options)
            self.addAction(a)
        self.addSeparator()

    def _update_filters(self):
        a = self.sender()
        self.filters[a.data()].setEnabled(a.isChecked())

    def _update_options(self):
        a = self.sender()
        self.options[a.data()][1] = a.isChecked()

    def columns(self, model_prefix):
        model_filters = [filterKey for filterKey in self.filters if filterKey.startswith(model_prefix)]
        return [self.filters[filterKey].modelColumn() for filterKey in model_filters if (self.filters[filterKey].enabled() or self.filters["All"].enabled())]

    def case_sensitive(self):
        return self.options["CS"][1]

    def match_words(self):
        return self.options["MatchWords"][1]
