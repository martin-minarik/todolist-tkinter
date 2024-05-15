import logging


API_URL = "http://127.0.0.1:5000"


def setup_logger():
    file_handler = logging.FileHandler('logfile.log')
    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
