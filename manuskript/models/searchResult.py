#!/usr/bin/env python
# --!-- coding: utf8 --!--


class searchResult():
    def __init__(self, model_type, model_id, column, title, path, pos):
        self._type = model_type
        self._id = model_id
        self._column = column
        self._title = title
        self._path = path
        self._pos = pos

    def type(self):
        return self._type

    def id(self):
        return self._id

    def column(self):
        return self._column

    def title(self):
        return self._title

    def path(self):
        return self._path

    def pos(self):
        return self._pos

    def __repr__(self):
        return "(%s, %s, %s, %s, %s, %s)" % (self._type, self._id, self._column, self._title, self._path, self._pos)

    def __eq__(self, other):
        return self.type() == other.type() and \
               self.id() == other.id() and \
               self.column == other.column and \
               self.startPos == other.startPos and \
               self.endPos == other.endPos
