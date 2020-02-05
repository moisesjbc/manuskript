#!/usr/bin/env python
# --!-- coding: utf8 --!--

from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QTextEdit, QTableView, QLineEdit, QPlainTextEdit, QListView, QComboBox
from PyQt5.QtCore import QItemSelectionModel


class widgetSelectionHighlighter():
    """
    Utility class for highlighting a selection on a widget.
    """
    def highlightWidgetSelection(self, widget, startPos, endPos):
        """
        Main method. Delegates the call to the right highlighting method according to the widget type.

        :param widget:      widget containing the result to be highlighter
        :param startPos:    starting position of the search result on the widget. Can be a cursor position, a row, etc
                            depending on the widget type.
        :param endPos:      ending position of the search result on the widget.
        """
        if isinstance(widget, QTextEdit) or isinstance(widget, QPlainTextEdit):
            self._highlightTextEditSearchResult(widget, startPos, endPos)
        elif isinstance(widget, QLineEdit):
            self._highlightLineEditSearchResult(widget, startPos, endPos)
        elif isinstance(widget, QTableView):
            self._highlightTableViewSearchResult(widget, startPos)
        elif isinstance(widget, QListView):
            self._highlightListSearchResult(widget, startPos)
        elif isinstance(widget, QComboBox):
            self._highlightComboBoxSearchResult(widget)
        else:
            raise NotImplementedError

        widget.setFocus(True)

    @staticmethod
    def generateClearHandler(widget, clear_callback):
        """
        Generates a clear handler to be run when the given widget loses focus.

        :param widget: widget we want to attach the handler to
        :param clear_callback: callback to be called when the given widget loses focus.
        :return:
        """
        def clear_handler(_widget, previousOnFocusOutEvent):
            clear_callback(_widget)
            _widget.focusOutEvent = previousOnFocusOutEvent

        old_widget_focus_out_event = widget.focusOutEvent
        widget.focusOutEvent = lambda e: clear_handler(widget, old_widget_focus_out_event)

    def _highlightTextEditSearchResult(self, text_edit, startPos, endPos):
        # On focus out, clear text edit selection.
        old_text_cursor = text_edit.textCursor()
        self.generateClearHandler(text_edit, lambda widget: widget.setTextCursor(old_text_cursor))

        # Highlight search result on the text edit.
        c = text_edit.textCursor()
        c.setPosition(startPos)
        c.setPosition(endPos, QTextCursor.KeepAnchor)
        text_edit.setTextCursor(c)

    def _highlightLineEditSearchResult(self, line_edit, startPos, endPos):
        # On focus out, clear line edit selection.
        self.generateClearHandler(line_edit, lambda widget: widget.deselect())

        # Highlight search result on line edit.
        line_edit.setCursorPosition(startPos)
        line_edit.cursorForward(True, endPos - startPos)

    def _highlightTableViewSearchResult(self, table_view, startPos):
        # On focus out, clear table selection.
        self.generateClearHandler(table_view, lambda widget: widget.clearSelection())

        # Highlight table row containing search result.
        table_view.selectRow(startPos)

    def _highlightListSearchResult(self, list_view, startPos):
        # On focus out, clear list selection
        currentIndex = list_view.currentIndex()
        self.generateClearHandler(list_view, lambda widget: widget.setCurrentIndex(currentIndex))

        # Highlight list row containing search result.
        index = list_view.model().index(startPos, 0, list_view.rootIndex())
        if index.isValid():
            list_view.setCurrentIndex(index)
            list_view.selectionModel().select(index, QItemSelectionModel.Select)

    def _highlightComboBoxSearchResult(self, comboBox):
        # On focus out, clear combo box highlighting.
        old_style = comboBox.styleSheet()
        self.generateClearHandler(comboBox, lambda widget: widget.setStyleSheet(old_style))

        # Highlight combo box.
        comboBox.setStyleSheet(old_style + " background-color: steelblue;")
