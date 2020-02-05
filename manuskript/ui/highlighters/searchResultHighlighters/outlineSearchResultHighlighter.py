#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.models import references as Ref
from manuskript.enums import Outline
from manuskript.ui.highlighters.searchResultHighlighters.modelSearchResultHighlighter import modelSearchResultHighlighter
from manuskript.functions import mainWindow
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QComboBox
from manuskript.ui.views.metadataView import metadataView
from manuskript.ui.collapsibleGroupBox2 import collapsibleGroupBox2


class outlineSearchResultHighlighter(modelSearchResultHighlighter):
    """
    Highlighter for search results on outline items
    """
    def __init__(self):
        super().__init__()
        self.outline_index = None

    def openView(self, searchResult):
        """
        Open the outline view containing the given search result
        """
        r = Ref.textReference(searchResult.id())
        Ref.open(r)

    def retrieveWidget(self, searchResult):
        """
        Retrieves the widget containing the given search result.

        Internally uses a map associating every searchable column to a tuple (widgetName, widgetType, parentName) where:

            - widgetName and widgetType:    name and type of the widget containing the searched column.
            - parentName:                   (Optional) Name of the parent widget. Used for visibility purposes.
        """
        editors = {
            Outline.text: ("txtRedacText", QTextEdit, None),
            Outline.title: ("txtTitle", QLineEdit, "grpProperties"),
            Outline.summarySentence: ("txtSummarySentence", QLineEdit, "grpSummary"),
            Outline.summaryFull: ("txtSummaryFull", QTextEdit, "grpSummary"),
            Outline.notes: ("txtNotes", QTextEdit, "grpNotes"),
            Outline.POV: ("cmbPOV", QComboBox, "grpProperties"),
            Outline.status: ("cmbStatus", QComboBox, "grpProperties"),
            Outline.label: ("cmbLabel", QComboBox, "grpProperties")
        }

        widgetName, widgetType, parentName = editors[searchResult.column()]

        # Most of metadata columns are inside a splitter widget that may be hidden, so we show these.
        if parentName:
            metadata_view = mainWindow().findChild(metadataView, "redacMetadata")
            metadata_view.show()
            metadata_view.findChild(collapsibleGroupBox2, parentName).button.setChecked(True)
            widget = metadata_view.findChild(widgetType, widgetName)
        else:
            widget = mainWindow().mainEditor.currentEditor().findChild(widgetType, widgetName)

        return widget
