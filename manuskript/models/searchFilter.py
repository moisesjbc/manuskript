#!/usr/bin/env python
# --!-- coding: utf8 --!--


class searchFilter:
    def __init__(self, label, enabled, modelColumn = None):
        if not isinstance(label, str):
            raise TypeError("label must be a str")

        if not isinstance(enabled, bool):
            raise TypeError("enabled must be a bool")

        if modelColumn is not None and (not isinstance(modelColumn, int) or isinstance(modelColumn, bool)):
            raise TypeError("modelColumn must be an int or None")

        self._label = label
        self._enabled = enabled
        self._modelColumn = modelColumn

    def label(self):
        return self._label

    def enabled(self):
        return self._enabled

    def modelColumn(self):
        return self._modelColumn

    def setEnabled(self, enabled):
        self._enabled = enabled
