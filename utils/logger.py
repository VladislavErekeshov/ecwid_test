import logging


class Logger:

    @staticmethod
    def log(level, message, file='logs.txt'):
        logging.basicConfig(level=logging.INFO, filename=file, filemode="a",
                            format="%(asctime)-12s %(levelname)s %(message)s",
                            datefmt="%d-%m-%Y %H:%M:%S")

        if level == 'INFO': logging.info(message)
        if level == 'WARNING': logging.warning(message)
        if level == 'ERROR': logging.error(message)
        if level == 'CRITICAL': logging.critical(message)
