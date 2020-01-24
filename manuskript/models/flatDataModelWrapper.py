#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.enums import FlatData

from manuskript.models.searchableModel import searchableModel
from manuskript.functions import search
from manuskript.models.searchResult import searchResult
from manuskript.enums import SearchModel


class flatDataModelWrapper(searchableModel):
    """
    All searches are performed on models inheriting from searchableModel, but special metadata such as book summaries
    are stored directly on a GUI element (QStandardItemModel). We wrap this GUI element inside this wrapper class
    so it exposes the same interface for searches.
    """
    def __init__(self, qStandardItemModel, tr):
        self.qStandardItemModel = qStandardItemModel
        self.tr = tr

    def column_info(self, column):
        column_data = {
            FlatData.summarySituation: (0, self.tr("Situation"), "{}".format(self.tr("Summary"))),
            FlatData.summarySentence: (1, self.tr("One sentence summary"), "{}".format(self.tr("Summary"))),
            FlatData.summaryPara: (2, self.tr("One paragraph summary"), "{}".format(self.tr("Summary"))),
            FlatData.summaryPage: (3, self.tr("One page summary"), "{}".format(self.tr("Summary"))),
            FlatData.summaryFull: (4, self.tr("Full summary"), "{}".format(self.tr("Summary")))
        }
        columnIndex, columnTitle, columnPath = column_data[column]
        return self.qStandardItemModel.item(1, columnIndex).text(), columnTitle, columnPath

    def searchOccurrences(self, searchRegex, columns):
        results = []

        for column in columns:
            columnText, columnTitle, columnPath = self.column_info(column)
            results += [searchResult(SearchModel.flatData, None, column, columnTitle, columnPath, (start, end)) for start, end in search(searchRegex, columnText)]
        return results
