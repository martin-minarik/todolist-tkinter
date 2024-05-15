import customtkinter as ctk
from .view import View
from .custom_widgets import Table
import client.views.styles as styles


class MainView(View):

    def __init__(self, parent):
        super().__init__(parent)

        self._create_widgets()
        self._set_layout()

    def _create_widgets(self):
        self.header_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.body_frame = ctk.CTkFrame(self.parent, fg_color="transparent")

        self.header_left_frame = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        self.title_label = ctk.CTkLabel(self.header_left_frame, text="To do", font=styles.title_font,
                                        anchor="w")

        self.header_right_frame = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        self.order_by_menu = ctk.CTkOptionMenu(self.header_right_frame, width=140,
                                               values=["Default Order",
                                                       "↑ Created", "↓ Created",
                                                       "↑ Due_to", "↓ Due_to",
                                                       "↑ Title", "↓ Title"])
        self.button_clear = ctk.CTkButton(self.header_right_frame,
                                          text="Clear",
                                          width=80,
                                          font=styles.button_font,
                                          fg_color="indianred")
        self.button_new = ctk.CTkButton(self.header_right_frame, text="New", width=80, font=styles.button_font)
        self.search_entry = ctk.CTkEntry(self.header_right_frame, width=140, placeholder_text="Search")

    def _set_layout(self):
        self.title_label.pack(side="top", fill="x", pady=4)

        self.order_by_menu.grid(row=0, column=0, padx=4, pady=4, sticky='e')
        self.button_clear.grid(row=0, column=1, padx=4, pady=4)
        self.search_entry.grid(row=1, column=0, padx=4, pady=4)
        self.button_new.grid(row=1, column=1, padx=4, pady=4)

        self.header_left_frame.pack(side="left")
        self.header_right_frame.pack(side="right")

        self.table = Table(self.body_frame)
        self.table.pack(expand=True, fill="both", padx=5, pady=5)

        self.header_frame.pack(side="top", fill="both", padx=10, pady=(10, 5))
        self.body_frame.pack(side="top", fill="both", expand=True)

    def _bind_commands(self):
        self.button_new.configure(command=self.controller.button_new_clicked)
        self.button_clear.configure(command=self.controller.button_clear_clicked)
        self.search_entry.bind('<Return>', self.controller.search_entry_enter)
        self.order_by_menu.configure(command=self.controller.order_by_action)
