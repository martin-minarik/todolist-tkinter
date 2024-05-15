import logging
import customtkinter as ctk
from views.main_view import MainView
from client.views import styles
from controllers.main_view_controller import MainViewController
import config


class App(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title('ToDo app')
        self.geometry("600x650")


def main():
    config.setup_logger()
    logging.info("Launching the application")

    app = App()

    ctk.set_appearance_mode("light")
    styles.init_styles()

    main_view = MainView(app)
    controller = MainViewController()

    main_view.set_controller(controller)
    controller.set_view(main_view)

    app.mainloop()


if __name__ == '__main__':
    main()
