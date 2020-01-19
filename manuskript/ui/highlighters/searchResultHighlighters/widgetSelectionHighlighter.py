#!/usr/bin/env python
# --!-- coding: utf8 --!--

from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QTextEdit, QTableView, QLineEdit, QPlainTextEdit, QLabel, QListView
from PyQt5.QtCore import QItemSelectionModel


class widgetSelectionHighlighter():
    """
    Utility class for highlighting a search result on a widget.
    """
    def __init__(self):
        pass

    def highlight_widget_selection(self, widget, start_pos, end_pos):
        if isinstance(widget, QTextEdit) or isinstance(widget, QPlainTextEdit):
            self._highlight_text_edit_search_result(widget, start_pos, end_pos)
        elif isinstance(widget, QLineEdit):
            self._highlight_line_edit_search_result(widget, start_pos, end_pos)
        elif isinstance(widget, QTableView):
            self._highlight_table_view_search_result(widget, start_pos)
        elif isinstance(widget, QListView):
            self._highlight_list_search_result(widget, start_pos)
        elif isinstance(widget, QLabel):
            self._highlight_label_search_result(widget)
        else:
            raise NotImplementedError

        widget.setFocus(True)

    @staticmethod
    def generate_clear_handler(widget, clear_callback):
        """
        Generates a clear handler to be run when the given widget loses focus.

        :param widget: widget we want to attach the handler to
        :param clear_callback: callback to be called when the given widget loses focus.
        :return:
        """
        def clear_handler(_widget, previous_on_focus_out_event):
            clear_callback(_widget)
            _widget.focusOutEvent = previous_on_focus_out_event

        old_widget_focus_out_event = widget.focusOutEvent
        widget.focusOutEvent = lambda e: clear_handler(widget, old_widget_focus_out_event)

    def _highlight_text_edit_search_result(self, text_edit, start_pos, end_pos):
        # On focus out, clear text edit selection.
        old_text_cursor = text_edit.textCursor()
        self.generate_clear_handler(text_edit, lambda widget: widget.setTextCursor(old_text_cursor))

        # Highlight search result on the text edit.
        c = text_edit.textCursor()
        c.setPosition(start_pos)
        c.setPosition(end_pos, QTextCursor.KeepAnchor)
        text_edit.setTextCursor(c)

    def _highlight_line_edit_search_result(self, line_edit, start_pos, end_pos):
        # On focus out, clear line edit selection.
        self.generate_clear_handler(line_edit, lambda widget: widget.deselect())

        # Highlight search result on line edit.
        line_edit.setCursorPosition(start_pos)
        line_edit.cursorForward(True, end_pos - start_pos)

    def _highlight_table_view_search_result(self, table_view, start_pos):
        # On focus out, clear table selection.
        self.generate_clear_handler(table_view, lambda widget: widget.clearSelection())

        # Highlight table row containing search result.
        table_view.selectRow(start_pos)

    def _highlight_list_search_result(self, list_view, start_pos):
        # On focus out, clear list selection
        current_index = list_view.currentIndex()
        self.generate_clear_handler(list_view, lambda widget: widget.setCurrentIndex(current_index))

        # Highlight list row containing search result.
        index = list_view.model().index(start_pos, 0, list_view.rootIndex())
        if index.isValid():
            list_view.setCurrentIndex(index)
            list_view.selectionModel().select(index, QItemSelectionModel.Select)

    def _highlight_label_search_result(self, label):
        # On focus out, clear label selection.
        # FIXME: This would overwrite all styles!
        old_style = label.styleSheet()
        self.generate_clear_handler(label, lambda widget: widget.setStyleSheet(old_style))

        # Highlight search result on label.
        label.setStyleSheet("background-color: steelblue")
