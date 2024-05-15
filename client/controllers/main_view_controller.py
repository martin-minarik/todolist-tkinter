from typing import TYPE_CHECKING
from .controller import Controller
from customtkinter import CTkToplevel
from .edit_view_controller import EditViewController
from client.views.edit_view import EditView

from client.controllers.endpoints import get_todo_records, delete_todo_records, search_todo_records

if TYPE_CHECKING:
    from ..views.main_view import MainView


class MainViewController(Controller):
    def __init__(self):
        super().__init__()
        self.todo_records = None
        self.search_keyword = None

    def set_view(self, view: "MainView"):
        self.view = view
        self.view.table.set_selection_callback(self.row_selected)
        self.view.table.set_convert_func_to_row(lambda x: (x.title, x.status, x.due_to.strftime("%m/%d/%Y, %H:%M:%S")))
        self.update_records()

    def button_new_clicked(self):
        controller = EditViewController()
        self._create_edit_window(controller)

    def button_clear_clicked(self):
        delete_todo_records()
        self.view.table.update_rows()

    def search_entry_enter(self, event):
        self.search_keyword = self.view.search_entry.get()
        self.update_records()

    def row_selected(self, index: int):
        controller = EditViewController(self.todo_records[index])
        self._create_edit_window(controller)

    def order_by_action(self, event):
        self.todo_records = self.sort_records(self.todo_records)
        self.update_table()

    def update_table(self):
        self.view.table.update_rows(self.todo_records)

    def update_records(self):
        self.fetch_todo_records()
        self.update_table()

    def fetch_todo_records(self):
        records = search_todo_records(self.search_keyword) if self.search_keyword else get_todo_records()
        sort_value = self.view.order_by_menu.get()
        self.todo_records = records if sort_value == "Default Order" else self.sort_records(records)

    def sort_records(self, records):
        value = self.view.order_by_menu.get()

        if value == "Default Order" or not value:
            return sorted(records, key=lambda card_data: card_data.id)

        direction, order_by = value.split()
        reverse = (direction != "↑")

        match order_by.lower():
            case "title":
                key = lambda card_data: card_data.title.lower()

            case "created":
                key = lambda card_data: card_data.created

            case "due_to":
                key = lambda card_data: card_data.due_to

            case _:
                raise ValueError("Invalid option for sorting")

        return sorted(records, key=key, reverse=reverse)

    def _create_edit_window(self, controller):
        new_window = CTkToplevel(self.view.parent, takefocus=True)
        new_window.title("edit")

        view = EditView(new_window)

        new_window.protocol("WM_DELETE_WINDOW",
                            lambda: (self.view.parent.grab_release(), new_window.destroy()))

        view.set_controller(controller)
        controller.set_callback_on_data_action(self.update_records)
        controller.set_view(view)

        new_window.after(100, new_window.focus)
        new_window.focus()
        new_window.grab_set()
