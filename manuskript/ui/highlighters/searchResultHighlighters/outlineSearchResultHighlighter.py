#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.models import references as Ref
from manuskript.enums import Outline
from manuskript.ui.highlighters.searchResultHighlighters.abstractSpecificSearchResultHighlighter import abstractSpecificSearchResultHighlighter
from manuskript.functions import mainWindow
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QLabel, QWidget, QGroupBox
from manuskript.ui.views.metadataView import metadataView
from manuskript.ui.collapsibleGroupBox2 import collapsibleGroupBox2


class outlineSearchResultHighlighter(abstractSpecificSearchResultHighlighter):
    def __init__(self):
        super().__init__()
        self.outline_index = None

    def open_view(self, search_result):
        r = Ref.textReference(search_result.id())
        Ref.open(r)

    def retrieve_widget(self, search_result):
        editors = {
            Outline.text: ("txtRedacText", QTextEdit, None),
            Outline.title: ("txtTitle", QLineEdit, "grpProperties"),
            Outline.summarySentence: ("txtSummarySentence", QLineEdit, "grpSummary"),
            Outline.summaryFull: ("txtSummaryFull", QTextEdit, "grpSummary"),
            Outline.notes: ("txtNotes", QTextEdit, "grpNotes"),

            # TODO: Tried to highlight the combo box themselves (ie. cmbPOV) but didn't succeed.
            Outline.POV: ("lblPOV", QLabel, "grpProperties"),
            Outline.status: ("lblStatus", QLabel, "grpProperties"),
            Outline.label: ("lblLabel", QLabel, "grpProperties")
        }

        editor_name, editor_class, parent_name = editors[search_result.column()]

        # Metadata columns are inside a splitter widget that my be hidden, so we show them.
        if parent_name:
            metadata_view = mainWindow().findChild(metadataView, "redacMetadata")
            metadata_view.show()
            metadata_view.findChild(collapsibleGroupBox2, parent_name).button.setChecked(True)
            widget = metadata_view.findChild(editor_class, editor_name)
        else:
            widget = mainWindow().mainEditor.currentEditor().findChild(editor_class, editor_name)

        return widget
