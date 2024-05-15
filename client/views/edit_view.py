import datetime
import customtkinter as ctk
import tkinter as tk
from .view import View
import client.views.styles as styles
from tkcalendar import DateEntry
from client.views.custom_widgets.spinbox import Spinbox
from datetime import datetime


class EditView(View):

    def __init__(self, parent):
        super().__init__(parent)

        # Variables
        self.title_var = tk.StringVar()
        self.status_var = tk.StringVar()
        self.created_var = tk.StringVar()
        self.last_edited_var = tk.StringVar()

        self._create_widgets()
        self._set_layout()

    def _create_widgets(self):

        # Tabview
        self.data_frame = ctk.CTkFrame(self.parent, width=200, height=200)

        # Card Data Tab
        self.label_title = ctk.CTkLabel(self.data_frame, text="Card Title:", font=styles.form_label_font)
        self.entry_title = ctk.CTkEntry(self.data_frame, textvariable=self.title_var)

        self.label_status = ctk.CTkLabel(self.data_frame, text="Status:", font=styles.form_label_font)
        self.menu_status = ctk.CTkOptionMenu(self.data_frame,
                                             values=["To read", "In progress", "Done"],
                                             variable=self.status_var)

        self.label_created_time = ctk.CTkLabel(self.data_frame, text="Created time:", font=styles.form_label_font)
        self.label_created_time_ = ctk.CTkLabel(self.data_frame, text="<created time>",
                                                textvariable=self.created_var)

        self.label_last_time_edited = ctk.CTkLabel(self.data_frame, text="Last time edited:",
                                                   font=styles.form_label_font)
        self.label_last_time_edited_ = ctk.CTkLabel(self.data_frame,
                                                    text="<last time edited>",
                                                    textvariable=self.last_edited_var)

        self.label_description = ctk.CTkLabel(self.data_frame, text="Description", font=styles.form_label_font)
        self.textbox_description = ctk.CTkTextbox(self.data_frame, corner_radius=10, fg_color="transparent",
                                                  border_width=2)

        # Datetime frame
        self.datetime_frame = ctk.CTkFrame(self.data_frame)
        self.label_due_to = ctk.CTkLabel(self.datetime_frame, text="Due to", font=styles.legend_label_font)
        self.label_date = ctk.CTkLabel(self.datetime_frame, text="Date:", font=styles.form_label_font)
        self.entry_date = DateEntry(self.datetime_frame, width=15, font=styles.button_font)
        self.label_hours = ctk.CTkLabel(self.datetime_frame, text="Hours", corner_radius=7)
        self.spinbox_hours = Spinbox(self.datetime_frame, minimum=0, maximum=24, start=0)
        self.label_minutes = ctk.CTkLabel(self.datetime_frame, text="Minutes", corner_radius=7)
        self.spinbox_minutes = Spinbox(self.datetime_frame, minimum=0, maximum=60, start=0)

        # Buttons
        self.button_save = ctk.CTkButton(self.parent, text="Save", width=80, font=styles.button_font)

        self.button_delete = ctk.CTkButton(self.parent, text="Delete", width=80, font=styles.button_font,
                                           fg_color="indianred")

    def _set_layout(self):
        # Datetime frame grid
        self.datetime_frame.grid_columnconfigure(1, weight=1)
        self.label_due_to.grid(row=0, column=0, padx=10, sticky="w")
        self.label_date.grid(row=1, column=0, padx=10, pady=10, sticky="se")
        self.entry_date.grid(row=1, column=1, padx=10, pady=10, sticky="se")

        self.label_hours.grid(row=2, column=0, padx=10, pady=10, sticky="se")
        self.spinbox_hours.grid(row=2, column=1, padx=10, pady=10, sticky="se")

        self.label_minutes.grid(row=3, column=0, padx=10, pady=10, sticky="se")
        self.spinbox_minutes.grid(row=3, column=1, padx=10, pady=10, sticky="se")

        # Card data grid
        self.data_frame.grid_columnconfigure(index=1, weight=1)
        self.data_frame.grid_rowconfigure(index=8, weight=1)
        self.label_title.grid(row=0, column=0, padx=10, pady=10, sticky="ne")
        self.entry_title.grid(row=0, column=1, padx=10, pady=10, sticky="se")

        self.label_status.grid(row=1, column=0, padx=10, pady=10, sticky="se")
        self.menu_status.grid(row=1, column=1, padx=10, pady=10, sticky="se")

        self.label_created_time.grid(row=2, column=0, padx=10, pady=10, sticky="se")
        self.label_created_time_.grid(row=2, column=1, padx=10, pady=10, sticky="se")

        self.label_last_time_edited.grid(row=3, column=0, padx=10, pady=10, sticky="se")
        self.label_last_time_edited_.grid(row=3, column=1, padx=10, pady=10, sticky="se")

        self.datetime_frame.grid(row=4, column=0, rowspan=4, columnspan=2, padx=10, pady=10, sticky="sew")

        self.label_description.grid(row=8, column=0, columnspan=2, padx=10, sticky="ws")
        self.textbox_description.grid(row=9, column=0, columnspan=2, padx=10, pady=(0, 5), sticky="sew")

        self.data_frame.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.button_save.pack(side="right", padx=10, pady=10)
        self.button_delete.pack(side="right", padx=10, pady=10)

    def _bind_commands(self):
        self.button_save.configure(command=self.controller.button_save_clicked)
        self.button_delete.configure(command=self.controller.button_delete_clicked)

    def init_vars(self, todo_record=None):
        if todo_record:
            self.title_var.set(todo_record.title)
            self.status_var.set(todo_record.status)
            self.created_var.set(todo_record.created.strftime("%Y-%m-%dT%H:%M:%S"))
            self.last_edited_var.set(todo_record.last_edited.strftime("%Y-%m-%dT%H:%M:%S"))
            self.spinbox_hours.set(todo_record.due_to.hour)
            self.spinbox_minutes.set(todo_record.due_to.minute)
            self.textbox_description.insert("0.0", todo_record.description)

        else:
            now = datetime.now().replace(microsecond=0)
            self.status_var.set("To do")
            self.created_var.set(str(now))
            self.last_edited_var.set(str(now))
