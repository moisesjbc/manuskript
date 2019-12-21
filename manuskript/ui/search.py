#!/usr/bin/env python
# --!-- coding: utf8 --!--
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QFontMetrics
from PyQt5.QtWidgets import QWidget, qApp, QListWidgetItem, QStyledItemDelegate, QStyle


from manuskript.functions import mainWindow
from manuskript.ui import style
from manuskript.ui.search_ui import Ui_search

from manuskript.models.flatDataModelWrapper import flatDataModelWrapper
from manuskript.models.searchableItem import searchResult
from manuskript.ui.searchMenu import searchMenu
from manuskript.ui.highlighters.searchResultHighlighters.searchResultHighlighter import searchResultHighlighter


class search(QWidget, Ui_search):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.searchTextInput.returnPressed.connect(self.search)

        self.searchMenu = searchMenu()
        self.btnOptions.setMenu(self.searchMenu)

        self.delegate = listResultDelegate(self)
        self.result.setItemDelegate(self.delegate)
        self.result.itemClicked.connect(self.openItem)

        self.result.setStyleSheet(style.searchResultSS())
        self.searchTextInput.setStyleSheet(style.lineEditSS())

        self.searchResultHighlighter = searchResultHighlighter()

    def prepare_regex(self, search_text):
        import re

        flags = re.UNICODE

        if self.searchMenu.case_sensitive() is not True:
            flags |= re.IGNORECASE

        # TODO: Apply re.escape conditionally once REGEX searches are implemented.
        search_text = re.escape(search_text)

        if self.searchMenu.match_words() is True:
            # Source: https://stackoverflow.com/a/15863102
            search_text = r'\b%s\b' % search_text

        return re.compile(search_text, flags)

    def search(self):
        self.result.clear()

        search_text = self.searchTextInput.text()
        if len(search_text) > 0:
            search_regex = self.prepare_regex(search_text)
            results = []

            # Set override cursor
            qApp.setOverrideCursor(Qt.WaitCursor)

            for model, model_prefix in [
                (mainWindow().mdlOutline, "Outline"),
                (mainWindow().mdlCharacter, "Character"),
                (flatDataModelWrapper(mainWindow().mdlFlatData, self.tr), "FlatData")
            ]:
                filtered_columns = self.searchMenu.columns(model_prefix)

                # Searching
                results += model.search_occurrences(search_regex, filtered_columns)

            print('results', results)

            # Showing results
            self.generate_results_lists(results)

            # Remove override cursor
            qApp.restoreOverrideCursor()

    def generate_results_lists(self, results):
        for result in results:
            # TODO: Results should be always a searchResult. Change method for outline.
            if isinstance(result, str):
                result = searchResult("Outline", str(result), None, 0)

            item = QListWidgetItem(result.title(), self.result)
            item.setData(Qt.UserRole, result)
            item.setData(Qt.UserRole + 1, result.path())
            self.result.addItem(item)

    def openItem(self, item):
        self.searchResultHighlighter.highlight_search_result(item.data(Qt.UserRole))

class listResultDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self, parent)

    def paint(self, painter, option, index):
        extra = index.data(Qt.UserRole + 1)
        if not extra:
            return QStyledItemDelegate.paint(self, painter, option, index)

        else:
            if option.state & QStyle.State_Selected:
                painter.fillRect(option.rect, option.palette.color(QPalette.Highlight))

            title = index.data()
            extra = " - {}".format(extra)
            painter.drawText(option.rect.adjusted(2, 1, 0, 0), Qt.AlignLeft, title)

            fm = QFontMetrics(option.font)
            w = fm.width(title)
            r = QRect(option.rect)
            r.setLeft(r.left() + w)
            painter.save()
            if option.state & QStyle.State_Selected:
                painter.setPen(Qt.white)
            else:
                painter.setPen(Qt.gray)
            painter.drawText(r.adjusted(2, 1, 0, 0), Qt.AlignLeft, extra)
            painter.restore()
