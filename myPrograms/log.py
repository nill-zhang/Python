#!/usr/bin/env python
# by sfzhang 2016.12.30

import logging
import sys
from logging import StreamHandler
from logging import FileHandler
# from logging import Formatter
# from logging.handlers import TimedRotatingFileHandler
# from logging.handlers import WatchedFileHandler


def test_logging():
    logging_formatter = "%(asctime)s:[%(levelname)s] %(message)s"
    logging_datefmt = "%b %d %H:%M:%S"
    logging.basicConfig(stream=sys.stdout, format=logging_formatter,
                        datefmt=logging_datefmt, level=logging.INFO)
    logging.error("An Error Happened")
    logging.warning("A Warning happened")
    logging.critical("A Critical happened")
    # the first can be a format string, the rest acts as substitutes
    logging.info("This is %s %s", "last", "one")
    # logging.INFO is 20, Custom Level above 20 will be printed
    custom_level = 100
    logging.addLevelName(custom_level, "CUSTOM_LEVEL")
    logging.log(custom_level, "This one is special")


def test_advanced_logging():
    # instantiate a stream handler
    console_handler = StreamHandler()
    console_fmt = "%(asctime)-30s-%(levelname)s-%(name)s-%(pathname)s-%(message)s-%()s"
    console_handler.setFormatter(fmt=console_fmt)
    console_handler.setLevel(logging.WARNING)

    # instantiate a file handler
    file_handler = FileHandler("advanced.log")
    file_fmt = "%(asctime)s-%(levelname)s-%(message)s"

    logger = logging.getLogger("file")
    logger.setLevel(logging.WARNING)
    logger.addHandler(console_handler)

    logger.error("This is an error")
    logger.critical("This is a critical")
    logger.warning("This is a warning")
    if logger.isEnabledFor(logging.INFO):
        logger.info("This is an info")


if __name__ == "__main__":
    test_logging()
    test_advanced_logging()


