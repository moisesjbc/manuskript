#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.models.abstractModel import abstractModel
from manuskript.models.searchableModel import searchableModel


class outlineModel(abstractModel, searchableModel):
    def __init__(self, parent):
        abstractModel.__init__(self, parent)

    def findItemsByPOV(self, POV):
        "Returns a list of IDs of all items whose POV is ``POV``."
        return self.rootItem.findItemsByPOV(POV)

    def searchOccurrences(self, searchRegex, columns):
        return self.rootItem.searchOccurrences(searchRegex, columns)
