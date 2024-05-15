from abc import ABC

import customtkinter


class LeftTopTabView(customtkinter.CTkTabview, ABC):
    _top_spacing: int = 0

    def _set_grid_segmented_button(self):
        self._segmented_button.grid(row=1, rowspan=2, column=0, columnspan=1,
                                    padx=self._apply_widget_scaling(self._corner_radius), sticky="w")

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
