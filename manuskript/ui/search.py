#!/usr/bin/env python
# --!-- coding: utf8 --!--
import re
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QFontMetrics
from PyQt5.QtWidgets import QWidget, qApp, QListWidgetItem, QStyledItemDelegate, QStyle


from manuskript.functions import mainWindow
from manuskript.ui import style
from manuskript.ui.search_ui import Ui_search

from manuskript.models.flatDataModelWrapper import flatDataModelWrapper
from manuskript.ui.searchMenu import searchMenu
from manuskript.ui.highlighters.searchResultHighlighters.searchResultHighlighter import searchResultHighlighter

from manuskript.enums import SearchOption, SearchModel


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

    def prepareRegex(self, searchText):
        search_options = self.searchMenu.options()

        flags = re.UNICODE

        if SearchOption.caseSensitive not in search_options:
            flags |= re.IGNORECASE

        if SearchOption.regex not in search_options:
            searchText = re.escape(searchText)

        if SearchOption.matchWords in search_options:
            # Source: https://stackoverflow.com/a/15863102
            searchText = r'\b%s\b' % searchText

        return re.compile(searchText, flags)

    def search(self):
        self.result.clear()

        searchText = self.searchTextInput.text()
        if len(searchText) > 0:
            searchRegex = self.prepareRegex(searchText)
            results = []

            # Set override cursor
            qApp.setOverrideCursor(Qt.WaitCursor)

            for model, modelType in [
                (mainWindow().mdlOutline, SearchModel.outline),
                (mainWindow().mdlCharacter, SearchModel.character),
                (flatDataModelWrapper(mainWindow().mdlFlatData, self.tr), SearchModel.flatData),
                (mainWindow().mdlWorld, SearchModel.world),
                (mainWindow().mdlPlots, SearchModel.plot)
            ]:
                # Searching
                columns = self.searchMenu.columns(modelType)
                if len(columns) > 0:
                    results += model.searchOccurrences(searchRegex, self.searchMenu.columns(modelType))

            self.lblResultsCounter.setText(self.generateResultsCountText(len(results)))

            # Showing results
            self.generateResultsLists(results)

            # Remove override cursor
            qApp.restoreOverrideCursor()
        else:
            self.lblResultsCounter.setText(self.generateResultsCountText(0))

    def onDataChanged(self):
        if len(self.searchTextInput.text()):
            self.search()

    def generateResultsCountText(self, nResults):
        if nResults == 0:
            return self.tr("No results found")
        elif nResults == 1:
            return self.tr("1 result found")
        else:
            return self.tr("{} results found").format(nResults)

    def generateResultsLists(self, results):
        modelPathPrefixes = {
            SearchModel.outline: self.tr("Outline"),
            SearchModel.character: self.tr("Characters"),
            SearchModel.flatData: self.tr("Flat data"),
            SearchModel.world: self.tr("World"),
            SearchModel.plot: self.tr("Plots"),
            SearchModel.plotStep: self.tr("Plots")
        }

        for result in results:
            path = modelPathPrefixes[result.type()]
            if len(result.path()) > 0:
                path += " > " + result.path()

            item = QListWidgetItem(result.title(), self.result)
            item.setData(Qt.UserRole, result)
            item.setData(Qt.UserRole + 1,  path)
            self.result.addItem(item)

    def openItem(self, item):
        self.searchResultHighlighter.highlightSearchResult(item.data(Qt.UserRole))

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
