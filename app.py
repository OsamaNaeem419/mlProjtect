import sys
from src.mlproject.logger import logging
from src.mlproject.exception import customException


if __name__ == "__main__":
    logging.info("Starting the application")
    try:
        a = 1 / 0
    except Exception as e:
        logging.error("Exception occurred")
        raise customException(e, sys)