from typing import TYPE_CHECKING, Callable
from client.model.todo_record import TodoRecord
from client.controllers.endpoints import delete_todo_record, create_todo_record, update_todo_record
from .controller import Controller
from datetime import datetime, time
from tkinter import messagebox

if TYPE_CHECKING:
    from client.views.edit_view import EditView


class EditViewController(Controller):
    def __init__(self, todo_record: TodoRecord = None):
        super().__init__()



        self.todo_record = todo_record
        self.callback_data_action = None

    def set_callback_on_data_action(self, callback: Callable):
        self.callback_data_action = callback

    def set_view(self, view: "EditView"):
        self.view = view
        self.view.init_vars(self.todo_record)

    def button_save_clicked(self):
        if not self.view.title_var.get():
            messagebox.showwarning("Warning", "Invalid title")
            return

        due_to = datetime.combine(self.view.entry_date.get_date(),
                                  time(self.view.spinbox_hours.get(),
                                       self.view.spinbox_minutes.get()))

        if self.todo_record:
            self.todo_record.title = self.view.title_var.get()
            self.todo_record.status = self.view.status_var.get()
            self.todo_record.due_to = due_to
            self.todo_record.description = self.view.textbox_description.get("0.0", "end")

            update_todo_record(self.todo_record)
        else:
            todo_record = TodoRecord(id=None,
                                     title=self.view.title_var.get(),
                                     status=self.view.status_var.get(),
                                     created=None,
                                     last_edited=None,
                                     due_to=due_to,
                                     description=self.view.textbox_description.get("0.0", "end"))
            create_todo_record(todo_record)

        if self.callback_data_action:
            self.callback_data_action()

        self.view.parent.destroy()

    def button_delete_clicked(self):
        if self.todo_record:
            delete_todo_record(self.todo_record)
            self.callback_data_action()

        self.view.parent.destroy()

