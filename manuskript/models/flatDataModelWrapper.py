#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.enums import FlatData

from manuskript.models.searchableModel import searchableModel
from manuskript.functions import search
from manuskript.models.searchResult import searchResult


class flatDataModelWrapper(searchableModel):
    """
    All searches are performed on models inheriting from searchableModel, but special metadata such as book summaries
    are stored directly on a GUI element (QStandardItemModel). We wrap this GUI element inside this wrapper class
    so it exposes the same interface for searches.
    """
    def __init__(self, qstandard_item_model, tr):
        self.qstandard_item_model = qstandard_item_model
        self.tr = tr

    def column_info(self, column):
        column_data = {
            FlatData.summarySituation: (0, self.tr("Situation"), "{}".format(self.tr("Summary"))),
            FlatData.summarySentence: (1, self.tr("One sentence summary"), "{}".format(self.tr("Summary"))),
            FlatData.summaryPara: (2, self.tr("One paragraph summary"), "{}".format(self.tr("Summary"))),
            FlatData.summaryPage: (3, self.tr("One page summary"), "{}".format(self.tr("Summary"))),
            FlatData.summaryFull: (4, self.tr("Full summary"), "{}".format(self.tr("Summary")))
        }
        column_index, column_title, column_path = column_data[column]
        return self.qstandard_item_model.item(1, column_index).text(), column_title, column_path

    def search_occurrences(self, search_regex, columns):
        results = []

        for column in columns:
            column_text, column_title, column_path = self.column_info(column)
            results += [searchResult("FlatData", None, column, column_title, column_path, (start, end)) for start, end in search(search_regex, column_text)]
        return results
