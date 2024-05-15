import customtkinter as ctk
from tkinter import ttk
from typing import Callable, List


class Table(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items = None
        self.selection_callback = None
        self.convert_func_to_row = None

        columns = ("title", 'status', 'due to')
        self.tree = ttk.Treeview(self, columns=columns, show='headings', style="table.Treeview")


        self.tree.heading('title', text='Title')
        self.tree.heading('status', text='Status')
        self.tree.heading('due to', text='Due To')

        self.tree.bind('<<TreeviewSelect>>', self._selected_item)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ctk.CTkScrollbar(self, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='nse')

    def set_selection_callback(self, callback: Callable):
        self.selection_callback = callback

    def clear(self):
        self.tree.selection_remove(*self.tree.selection())
        for item in self.tree.get_children():
            self.tree.delete(item)

    def _selected_item(self, event):
        if self.tree.selection():
            item_index = self.tree.index(self.tree.selection()[0])
            if self.selection_callback:
                self.selection_callback(item_index)

    def set_convert_func_to_row(self, convert_func: Callable):
        self.convert_func_to_row = convert_func

    def update_rows(self, items=None):
        self.clear()
        if items:
            for item in items:
                self.tree.insert('', 'end', values=self.convert_func_to_row(item))
